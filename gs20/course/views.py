from django.shortcuts import render
from . models import DjangoCourse

# Create your views here.

def course(request):
    djangoCourse = DjangoCourse.objects.all()
    return render(request, 'course/course.html',{'djangoCourse': djangoCourse})