# Recipe App

The Recipe App is a **Django-based web application** that enables users to explore, manage, and search for recipes seamlessly. Designed with an intuitive interface and rich features, the app caters to cooking enthusiasts by offering dynamic visualizations, an elegant recipe browser, and an interactive recipe management system.

---

## Features

### Core Functionalities
- **Search Recipes**:
  - Easily search recipes by **name** or **ingredients**.
  - Supports advanced search with **multiple ingredient filters** and **partial matches**.
  
- **View Recipes**:
  - Detailed recipe pages with images and all relevant information (ingredients, cooking time, and difficulty).
  - Recipes are displayed in a stylish grid layout for easy browsing.

- **Add Recipes**:
  - Users can add new recipes via a simple and user-friendly form.
  - Recipes include **name**, **ingredients**, **cooking time**, and optional images.
  - Automatic calculation of **difficulty level** based on cooking time and the number of ingredients.

### Enhanced Features
- **Chart Visualizations**:
  - Interactive visualizations based on user searches:
    - **Bar Chart**: Displays cooking times for recipes.
    - **Pie Chart**: Visualizes the distribution of cooking times across recipes.
    - **Line Chart**: Shows the trend of cooking times for searched recipes.
  - Charts are dynamically generated using **Matplotlib**.

- **Search Results**:
  - Results are presented in a **styled and responsive table**.
  - Includes clickable links to navigate to recipe detail pages.

- **About Me Page**:
  - A personalized "About Me" page with information about the developer, contact links, and GitHub portfolio.

---

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS, and JavaScript for interactivity and responsiveness.
- **Database**: SQLite (default) with Django ORM.
- **Data Visualization**: Matplotlib for creating charts.
- **Testing**: Comprehensive unit tests for models, forms, and views.

---

## Getting Started

### Prerequisites
- Python 3.8 or above installed on your system.
- Virtual environment setup (recommended for dependency management).

### Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/recipe-app.git
   cd recipe-app

2. Create a virtual environment and activate it:
   python -m venv env
   source env/bin/activate   # For Linux/MacOS
   env\Scripts\activate      # For Windows

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run database migrations:
   python manage.py migrate

5. Create a superuser for the admin panel:
   python manage.py createsuperuser

6. Start the development server:
   python manage.py runserver

7. Open the app in your browser at:
   http://127.0.0.1:8000