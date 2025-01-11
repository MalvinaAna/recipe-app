from django import forms

CHART_CHOICES = (
    ('bar', 'Bar Chart'),
    ('pie', 'Pie Chart'),
    ('line', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(required=False, label='Recipe Name')
    ingredients = forms.CharField(required=False, label='Ingredients (comma-separated)')
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False, label='Chart Type')