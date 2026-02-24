from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dj_fee(request):
    return render(request, 'fees/feesone.html')

def py_fee(request):
    return render(request, 'fees/feestwo.html')