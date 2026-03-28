from urllib import request

from django.shortcuts import render
from . models import Menucatagory 
# Create your views here.

def home(request):
    items = Menucatagory.objects.all() 
    return render(request, 'core/home.html', {'items': items})