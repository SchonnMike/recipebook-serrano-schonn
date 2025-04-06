from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm
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
    # handle multiple forms at once
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=3)

    if request.method == "POST":
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for ingredient_form in formset:
                # save each ingredient form
                ingredient = ingredient_form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            
            return redirect('ledger:tasks', num=recipe.id)
        
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    recipes = Recipe.objects.all()

    return render(request, 'add_recipe.html', {'form': form, 'formset': formset, 'recipes': recipes})

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