from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from django.contrib.auth.models import User

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

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(admin.ModelAdmin):
	inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)