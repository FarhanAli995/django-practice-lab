from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def StudentFee(request):
#     return render(request, 'StudentFee.html')


def StudentFee(request):
    return HttpResponse('Here you will get Student Fee details')

def firstYearStu(request):
    return HttpResponse('<h1>Here you will get Student Fee details of 1st year</h1><p> The following are 1st Year Students.</p>')