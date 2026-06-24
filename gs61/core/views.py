from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    if request.method == "POST":
        fm = forms.RegistrationForm(request.POST, request.FILES)
        if fm.is_valid():
            username = fm.cleaned_data["username"]
            age = fm.cleaned_data["age"]
            resume = fm.cleaned_data["resume"]
            print("Form is valid")
            return render(request, "core/success.html", {"form": fm})
    else:
        fm = forms.RegistrationForm()
    return render(request, "core/home.html", {"form": fm})