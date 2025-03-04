from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def basicParams(request):
    # recipe list
    recipes = Recipe.objects.all()
    return render(request, 'basicParams.html', {'recipes': recipes})

def tasks(request, num):
    # recipe task
    recipe = Recipe.objects.get(id=num)
    return render(request, 'task_list.html', {'recipe':recipe})
