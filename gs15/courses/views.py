from django.shortcuts import render

# Create your views here.

def course_1(request):
    return render(request,'courses/course_1.html')
