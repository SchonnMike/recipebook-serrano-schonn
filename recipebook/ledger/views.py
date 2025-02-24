from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse("hello world")

def basicTemplate(request):
    return render(request, 'basicParams.html')

def basicParams(request, num=1):
    if num == 1:
        number = "first"
    elif num ==2:
        number = "second"
    else:
        number = "nth"
    return render(request, 'basicParams.html', {'number': number})

def tasks(request):
    ctx = {
        'tasks':[
            "task1",
            "task2",
            "task3",
            "task4"
        ]
    }
    return render(request, 'task_list.html', ctx)
