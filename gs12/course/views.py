from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_dj(request):
    coursename = {
        'cname': 'Django',
        'StudentName': 'Farhan Ali',
        'Duration': '6 Months',
        'seats': '10'
        }
    return render(request, 'course/courseone.html',
     coursename)

def learn_py(request):
    return HttpResponse("python!")