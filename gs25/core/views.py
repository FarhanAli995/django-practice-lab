from django.shortcuts import render
from .form import StudentsData, Teachers

# Create your views here.
def stud_data(request):

    form = StudentsData(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)

    context = {
        'data': form
    }

    return render(request, 'core/home.html', context)

def teachers(request):
    teach = 'core/teacher.html'
   
    form = Teachers(request.GET)
    if request.method == 'GET':
        if form.is_valid():
            print(form.cleaned_data)

        else:
            print(form.errors)

        context = {
        'data': form
        }


    return render(request, 'core/teachers.html', context)