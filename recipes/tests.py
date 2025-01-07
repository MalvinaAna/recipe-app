from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Soup',
            ingredients='water, carrot, potato, salt',
            cooking_time=15,
            image="recipes/sample.jpg"
        )

    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_ingredients_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name

        self.assertEqual(field_label, 'ingredients')

    def test_cooking_time_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name

        self.assertEqual(field_label, 'cooking time')

    def test_difficulty_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('difficulty').verbose_name

        self.assertEqual(field_label, 'difficulty')

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length

        self.assertEqual(max_length, 50)  

    def test_object_str_is_name(self):
        recipe = Recipe.objects.get(id=1)

        self.assertEqual(str(recipe), recipe.name)

    def test_difficulty(self):
          recipe = Recipe.objects.get(id=1)
          recipe.calculate_difficulty()
          self.assertEqual(recipe.difficulty, "Intermediate")

    def test_get_absolute_url(self):
          recipe = Recipe.objects.get(id=1)
          self.assertEqual(recipe.get_absolute_url(), '/list/1')