# Recipe App

The Recipe App is a Django-based web application that allows users to explore, manage, and search for recipes. With an intuitive interface and powerful features, users can find and visualize their favorite recipes effortlessly. This project is designed to provide a seamless experience for users who love to cook and explore new recipes.

## Features

### Core Functionalities
- **Search Recipes**:
  - Search recipes by name or specific ingredients.
  - Supports advanced search with multiple ingredient filters and partial matches.

- **View Recipes**:
  - Recipe detail pages are styled with images and all relevant information.
  - Recipes are displayed in a grid layout for easy browsing.

### Enhanced Features
- **Chart Visualizations**:
  - **Bar Chart**: Displays cooking times for each recipe.
  - **Pie Chart**: Visualizes the distribution of cooking times across recipes.
  - **Line Chart**: Shows the trend of cooking times across different recipes.
  - Charts are dynamically generated based on user searches.

- **Search Results**:
  - Results are displayed in a styled table, ensuring consistency with the app's design.
  - The table includes clickable recipe links that navigate to the detailed recipe page.

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS
- **Database**: SQLite (default) with Django ORM
- **Data Visualization**: Matplotlib
- **Testing**: Comprehensive unit tests for models, forms, and views
