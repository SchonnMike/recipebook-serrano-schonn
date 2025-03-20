from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def basicParams(request):
    # recipe list
    recipes = Recipe.objects.all()
    return render(request, 'basicParams.html', {'recipes': recipes})

def tasks(request, num):
    # recipe task
    recipe = Recipe.objects.get(id=num)
    return render(request, 'task_list.html', {'recipe':recipe})
