from django.shortcuts import render
# Create your views here.

def stu_details(request):
    return render(request, 'root/students.html')