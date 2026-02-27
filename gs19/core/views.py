from django.shortcuts import render
from . models import Students

# Create your views here.

def home(request):
    students = Students.objects.all()
    return render(request, 'core/home.html', {"students": students})