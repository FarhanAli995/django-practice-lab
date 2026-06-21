from django.shortcuts import render
from .form import StuReg

def showdata(request):
    if request.method == "POST":
        fm = StuReg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            print("Form is valid")
            
        return render(request, "core/success.html", {"form": fm})
    else:
        fm = StuReg()
    return render(request, "core/home.html", {"form": fm})

