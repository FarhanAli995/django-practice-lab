from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse('Hello Django')


def django(request):
    return HttpResponse('my name is ')

def learn_python(request):
    return HttpResponse('Hello Python')

def best_course(request):
    return HttpResponse('welocome Django full single shot course!')

# def learn_django(request):
#     return HttpResponse('Hello Django')














