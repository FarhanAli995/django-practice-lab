from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def StudentFee(request):
#     return render(request, 'StudentFee.html')


def StudentFee(request):
    return HttpResponse('Here you will get Student Fee details')