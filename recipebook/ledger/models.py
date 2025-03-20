from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	year_level = models.IntegerField()
	course = models.CharField(max_length=10)