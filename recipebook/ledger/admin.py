from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)
    search_fields = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)