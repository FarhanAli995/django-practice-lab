from django.shortcuts import render

# Create your views here.

def home(request):
    ho= {
        'title' : 'Learn Django',
        'cname': 'Django.',
        'fees': 'Rs.300',
        "time": 3
    }
    return render(request, 'core/home.html',ho)
