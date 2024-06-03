import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Fridge Genie", page_icon="🍴")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1490645935967-10de6ba17061");
        background-attachment: fixed;
        background-size: cover;
        color: white;
    }}
    .blur-box {{
        background: rgba(290, 378, 289, 0.8);
        backdrop-filter: blur(90px); /* Increase the blur effect */
        -webkit-backdrop-filter: blur(90px); /* Increase the blur effect */
        border-radius: 15px;
        padding: 30px;
        max-width: 100%;
        width: 100%;
        margin: auto;
        margin-top: 50px;
        color: black;
        overflow: auto; /* Allow content to overflow and enable scrolling */
        height: 100vh; /* Set the height to the full viewport height */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: absolute; /* Position the blur box absolutely */
        top: 90%; /* Position the blur box at the center of the page */
        transform: translateY(-40%); /* Move the blur box up by half its height */
    }}
    .stTextInput > div > div > input, .stSelectbox > div > div {{
        background: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
    }}
    .stButton > button {{
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="blur-box">', unsafe_allow_html=True)
st.title("Fridge Genie: Your Personal Recipe Finder")

def get_recipes(ingredients, diet, cuisine, dish_type):
    # api_key = "<your-api-key>"
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": st.secrets["api_key"],
        "query": ingredients,
        "diet": diet if diet != "None" else None,
        "cuisine": cuisine if cuisine != "None" else None,
        "type": dish_type if dish_type != "None" else None,
        "number": 10,
        "addRecipeInformation": True,
        "addNutritionInformation": True
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    ingredients = st.text_input("Enter comma-separated ingredients (e.g. chicken, rice, broccoli): ")
    diet = st.selectbox("Dietary restrictions", ["None", "Vegetarian", "Vegan", "Gluten-Free", "Ketogenic"])
    cuisine = st.selectbox("Cuisine Type", ["None", "Italian", "Chinese", "Mexican", "Indian", "American", "Thai"])
    dish_type = st.selectbox("Dish Type", ["None", "Main Course", "Side Dish", "Dessert", "Appetizer", "Salad", "Bread", "Breakfast", "Soup", "Beverage", "Sauce", "Marinade", "Fingerfood", "Snack", "Drink"])

    if st.button("Find Recipes"):
        if ingredients:
            response = get_recipes(ingredients, diet, cuisine, dish_type)
            results = response.get("results", [])
            if len(results) == 0:
                st.write("No recipes found.")
            else:
                for recipe in results:
                    st.subheader(recipe["title"])
                    st.write(f"**Ready in:** {recipe['readyInMinutes']} minutes")
                    st.write(f"**Servings:** {recipe['servings']}")
                    if recipe.get("nutrition"):
                        st.write(f"**Calories:** {recipe['nutrition']['nutrients'][0]['amount']} kcal")
                    st.image(recipe["image"], use_column_width=True)
                    st.write(f"[View Recipe]({recipe['sourceUrl']})")
        else:
            st.write("Enter at least one ingredient")

if __name__ == "__main__":
    main()

st.markdown('</div>', unsafe_allow_html=True)
