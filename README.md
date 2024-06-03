# Fridge Genie: Your Personal Recipe Finder

Fridge Genie is a Streamlit-based web application that helps you find recipes based on the ingredients you have in your fridge.

## Features

- Search for recipes based on ingredients, dietary restrictions, cuisine, and dish type.
- View detailed information about the recipes, including preparation time, servings, and nutritional information.
- Easily access the recipe source URL to get the full instructions.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Streamlit
- Requests
- Pandas

### Installation

1. Clone the repository:
  git clone https://github.com/your-username/fridge-genie.git

2. Change to the project directory:
  cd fridge-genie

3. Install the required dependencies:
   pip install -r requirements.txt

4. Obtain an API key from Spoonacular and add it to your Streamlit secrets:
  streamlit secrets set api_key your-api-key-here

5. Run the application:
  streamlit run app.py

## Docker

You can also run the application using Docker. Build the Docker image and run the container:
  docker build -t fridge-genie .
  docker run -p 8501:8501 fridge-genie
