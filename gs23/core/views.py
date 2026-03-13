
from django.shortcuts import render
from core.forms import StudentRegistration
# Create your views here.

def showdata(request):
    data = StudentRegistration()
    return render(request, "core/user.html", {"data": data})
