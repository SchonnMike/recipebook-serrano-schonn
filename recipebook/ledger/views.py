from django.shortcuts import render
from django.http import HttpResponse

def basicParams(request):
    # recipe list
    recipes = Recipe.objects.all()
    return render(request, 'basicParams.html', {'recipes': recipes})

def tasks(request, num):
    # recipe task
    recipe = get_object_or_404(Recipe, id=num)
    return render(request, 'task_list.html', {'recipe':recipe})
