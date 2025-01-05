from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()  # Comma-separated ingredients
    cooking_time = models.PositiveIntegerField()  # Time in minutes
    difficulty = models.CharField(max_length=50, blank=True)  # Automatically calculated

    def __str__(self):
        return self.name

    def return_ingredients_as_list(self):
        return [ingredient.strip() for ingredient in self.ingredients.split(',')]

    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients <= 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients > 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients <= 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def save(self, *args, **kwargs):
        self.calculate_difficulty()
        super().save(*args, **kwargs)