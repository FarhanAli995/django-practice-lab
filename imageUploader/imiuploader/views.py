from django.shortcuts import render
from .models import Image

# Create your views here.

def home(request):
    stu = Image.objects.all()
    return render(request, 'imiuploader/home.html', {'stu': stu})