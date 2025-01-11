from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipesSearchForm, RecipeForm
import pandas as pd
from .utils import get_chart


# Home view
def home(request):
    return render(request, 'recipes/recipes_home.html')


# About Me view
def about_me(request):
    return render(request, 'recipes/about_me.html')


# Recipe List View
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Recipe.objects.all()
        recipe_name = self.request.GET.get('recipe_name', '')
        ingredients = self.request.GET.get('ingredients', '')

        if recipe_name:
            queryset = queryset.filter(name__icontains=recipe_name)
        if ingredients:
            ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
            for ingredient in ingredients_list:
                queryset = queryset.filter(ingredients__icontains=ingredient)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        form = RecipesSearchForm(self.request.GET or None)
        recipes_df = pd.DataFrame(list(queryset.values('name', 'ingredients', 'difficulty', 'cooking_time')))
        chart = None
        if not recipes_df.empty:
            chart_type = self.request.GET.get('chart_type', 'bar')
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].tolist())
        context.update({
            'form': form,
            'recipes_df': recipes_df.to_html(classes='table') if not recipes_df.empty else None,
            'chart': chart,
        })
        return context


# Recipe Detail View
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_details.html'


# Add Recipe View
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('recipes:list')