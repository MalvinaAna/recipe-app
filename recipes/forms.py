from django import forms
from .models import Recipe

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100, required=False)
    ingredients = forms.CharField(max_length=255, required=False)
    chart_type = forms.ChoiceField(choices=[('bar', 'Bar'), ('pie', 'Pie'), ('line', 'Line')], required=False)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'cooking_time', 'image']