from django import forms
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'