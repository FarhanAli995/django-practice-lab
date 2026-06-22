from django.shortcuts import render
from .form import CustomerForm

def home(request):
    if request.method == "POST":
        fm = CustomerForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            print("Form is valid")
            return render(request, "core/success.html", {"form": fm})
    else:
        fm = CustomerForm()
    return render(request, "core/home.html", {"form": fm})