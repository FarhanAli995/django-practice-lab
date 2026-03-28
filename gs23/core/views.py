
from django.shortcuts import render
from core.forms import StudentRegistration, TeacherRegistration
# Create your views here.

def showdata(request):
    data = StudentRegistration()
    return render(request, "core/user.html", {"data": data})

def show_teacher_data(request):
    data = TeacherRegistration()
    return render(request, "core/teacher.html", {"data": data})


