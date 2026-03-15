
from django.shortcuts import render
from core.forms import StudentRegistration, TeacherRegistration
# Create your views here.

def showdata(request):
    data = StudentRegistration()
    data.order_fields(field_order=['name', 'email', 'Phone_Number', 'Reg_Number', 'password'])
    return render(request, "core/user.html", {"data": data})

def show_teacher_data(request):
    data = TeacherRegistration()
    return render(request, "core/teacher.html", {"data": data})