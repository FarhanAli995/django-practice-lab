from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_dj(request):
    django_details ={
        'nm': 'Django is Awesome',
        'du':'4 Months'
    
    }
    return render(request, 'course/courseone.html', django_details)

def learn_py(request):
    return HttpResponse("python!")