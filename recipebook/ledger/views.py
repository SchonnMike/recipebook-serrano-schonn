from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("hello world")

def basicTemplate(request):
    return render(request, 'basicParams.html')
