from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    if request.method == "POST":
        fm = forms.loginform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            print("Form is valid")
            return render(request, "core/success.html", {"form": fm})
    else:
        fm = forms.loginform()
    return render(request, "core/home.html", {"loginform": fm})