from django.shortcuts import render, redirect # Make sure redirect is imported!


def home(request):
    return render(request, "root/home.html")