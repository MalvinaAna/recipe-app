from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe
from .forms import RecipesSearchForm


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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


class RecipeFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'recipe_name': 'Soup', 'ingredients': 'water, carrot'}
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # Create test recipes
        Recipe.objects.create(
            name="Soup",
            ingredients="water, carrot, salt",
            cooking_time=15,
            image="recipes/sample.jpg"
        )
        Recipe.objects.create(
            name="Salad",
            ingredients="lettuce, tomato, cucumber",
            cooking_time=5,
            image="recipes/sample2.jpg"
        )

    def setUp(self):
        # Log in the test user for views requiring authentication
        self.client.login(username='testuser', password='testpass')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Soup")
        self.assertContains(response, "Salad")
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    def test_recipe_detail_view(self):
        recipe = Recipe.objects.get(name="Soup")
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Soup")
        self.assertTemplateUsed(response, 'recipes/recipes_details.html')

    def test_search_functionality(self):
        response = self.client.get(reverse('recipes:list'), {'recipe_name': 'Soup'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Soup")
        self.assertNotContains(response, "Salad")