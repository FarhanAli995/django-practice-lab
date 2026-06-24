from django.shortcuts import render
from . import forms

def home(request):
    if request.method == "POST":
        fm = forms.StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            print(f"Form is valid! Registered {name}")
            return render(request, "core/success.html", {"form": fm})
    else:
        fm = forms.StudentRegistration()
    return render(request, "core/home.html", {"form": fm})