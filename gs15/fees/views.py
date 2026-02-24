from django.shortcuts import render

# Create your views here.

def fees_1(request):
    return render(request, 'fees/fees_1.html')