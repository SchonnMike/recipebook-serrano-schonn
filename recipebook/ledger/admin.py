from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)