from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm
from django.forms import modelformset_factory

@login_required
def basicParams(request):
    # recipe list
    recipes = Recipe.objects.all()
    return render(request, 'basicParams.html', {'recipes': recipes})

@login_required
def tasks(request, num):
    # recipe task
    recipe = Recipe.objects.get(id=num)
    return render(request, 'task_list.html', {'recipe':recipe})

@login_required
def add_recipe(request):
    # handle multiple forms at once (RecipeForm, RecipeIngredienForm, IngredientForm)
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=3)

    if request.method == "POST":

        if 'add_recipe' in request.POST:
            form = RecipeForm(request.POST)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('ledger:tasks', num=recipe.id)

        elif 'add_ingredient' in request.POST:
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
                return redirect('ledger:add_recipe')
                
        elif 'add_recipe_ingredient' in request.POST:
            formset = RecipeIngredientFormSet(request.POST)
            if formset.is_valid():
                for recipe_ingredient_form in formset:
                    if recipe_ingredient_form.cleaned_data:
                        # check each ingredient and selected recipe, then link and save
                        ingredient = recipe_ingredient_form.save(commit=False)
                        selected_recipe = recipe_ingredient_form.cleaned_data.get('recipe')
                        if selected_recipe:
                            ingredient.recipe = selected_recipe
                        ingredient.save()
                return redirect('ledger:tasks', num=selected_recipe.id)
        
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
        ingredient_form = IngredientForm()

    recipes = Recipe.objects.all()

    return render(request, 'add_recipe.html', {
        'form': form, 
        'formset': formset, 
        'ingredient_form': ingredient_form,
        'recipes': recipes,
    })

@login_required
def add_image(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('ledger:tasks', num=pk)
    else:
        form = RecipeImageForm()

    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})