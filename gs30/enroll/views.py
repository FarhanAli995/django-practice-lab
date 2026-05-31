from django.shortcuts import render
from .form import SignUpForm
# Create your views here.

def signup(request):
    form = SignUpForm()
    return render(request, "enroll/signup.html", {'form': form})
