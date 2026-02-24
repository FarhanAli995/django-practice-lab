from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learnDjango(request):
    return HttpResponse('Learn Django Course Here.')

def learnPython(request):
    return HttpResponse('Learn Python Course Here.')