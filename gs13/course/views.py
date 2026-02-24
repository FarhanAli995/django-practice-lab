# views.py

from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime

def learn_dj(request):
    
    courses = [
        {"name": "Django Basics", "duration": "1 Month", "level": "Beginner"},
        {"name": "Django REST API", "duration": "1.5 Months", "level": "Intermediate"},
        {"name": "Django Deployment", "duration": "2 Weeks", "level": "Advanced"},
    ]

    student_count = random.randint(100, 500)
    progress = random.randint(60, 100)

    context = {
        "title": "Advanced Django Course",
        "courses": courses,
        "students": student_count,
        "progress": progress,
        "today": datetime.now(),
        "images": [
            "https://picsum.photos/300/200?random=1",
            "https://picsum.photos/300/200?random=2",
            "https://picsum.photos/300/200?random=3",
            "https://picsum.photos/300/200?random=4",
        ]
    }

    return render(request, "course/courseone.html", context)


def learn_py(request):
    context_1 = {
        "name" :"Farhan Ali",
        "d" : datetime.now()
    }
    return render(request,"course/coursetwo.html",context_1)
