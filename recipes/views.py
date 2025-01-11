from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart

# Home view
def home(request):
    """
    Render the home page for the recipes app.
    """
    return render(request, 'recipes/recipes_home.html')


# Recipe list view with search and visualization
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        """
        Filter recipes based on search criteria provided via GET parameters.
        """
        queryset = Recipe.objects.all()  # Default to show all recipes
        recipe_name = self.request.GET.get('recipe_name', '')  # Get recipe name from query params
        ingredients = self.request.GET.get('ingredients', '')  # Get ingredients from query params

        if recipe_name:
            queryset = queryset.filter(name__icontains=recipe_name)  # Partial match for recipe name
        if ingredients:
            ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]  # Split ingredients
            for ingredient in ingredients_list:
                queryset = queryset.filter(ingredients__icontains=ingredient)  # Match each ingredient

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add search form, chart, and DataFrame to context for the template.
        """
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()  # Get filtered queryset
        form = RecipesSearchForm(self.request.GET or None)  # Create search form with GET data

        # Convert queryset to DataFrame and generate chart if results exist
        recipes_df = None
        chart = None
        if queryset.exists():
            recipes_df = pd.DataFrame(list(queryset.values('name', 'ingredients', 'difficulty', 'cooking_time')))
            if not recipes_df.empty:  # Check for non-empty DataFrame
                chart_type = self.request.GET.get('chart_type', 'bar')  # Default chart type is 'bar'
                chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].tolist())  # Generate chart

        # Add data to context
        context.update({
            'form': form,
            'chart': chart,
            'recipes_df': recipes_df.to_html(classes='table table-striped', index=False) if recipes_df is not None else None,
        })
        return context


# Recipe detail view
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_details.html'