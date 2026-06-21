from django.shortcuts import render
from .form import StuReg

def showdata(request):
    if request.method == "POST":
        fm = StuReg(request.POST)
        if fm.is_valid():
            print("Form is valid")
    else:
        fm = StuReg()
    return render(request, "core/home.html", {"form": fm})
