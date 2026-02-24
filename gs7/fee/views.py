from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def djangoFee(request):
    return HttpResponse('Rs.500!')

def pythonFee(request):
    return HttpResponse('Rs.300!')