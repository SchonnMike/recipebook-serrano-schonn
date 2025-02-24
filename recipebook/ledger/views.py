from django.shortcuts import render, HttpResponse

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
