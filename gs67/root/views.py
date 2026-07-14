from django.shortcuts import render

# Create your views here.

def home(request, year):
    stu = {"yr": year}
    return render(request, "root/home.html", stu)