from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loaderfor

recipes = [
    {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    },
    {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quanity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
]

def basicParams(request):
    # recipe list
    return render(request, 'basicParams.html', {'recipes': recipes})

def tasks(request, num):
    # recipe task
    if num == 1:
        recipe = recipes[0]
    elif num == 2:
        recipe = recipes[1]
    return render(request, 'task_list.html', {'recipe':recipe})
