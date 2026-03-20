from django.shortcuts import render
from .form import StudentsData, TeachersData

# Create your views here.
def stud_data(request):
    if request.method == 'POST':
        form = StudentsData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentsData()

    context = {
        'form': form
    }

    return render(request, 'core/home.html', context)

def teachers(request):
    teach = 'core/teacher.html'
   
    form = TeachersData(request.GET)
    if request.method == 'GET':
        if form.is_valid():
            print(form.cleaned_data)

        else:
            print(form.errors)

    context = {
    'data': form
    }


    return render(request, 'core/teachers.html', context)