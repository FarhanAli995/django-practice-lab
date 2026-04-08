from django.shortcuts import render
from .form import StudentRegistration

# Create your views here.

def home(request):
    form = StudentRegistration()
    return render(request, 'home.html', {'form': form})