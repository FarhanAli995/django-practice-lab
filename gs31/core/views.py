from django.shortcuts import render
from .forms import StudentForm
from django.contrib import messages

def register(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            form = StudentForm()

    else:
        form = StudentForm()

    return render(request,'core/signup.html',{'form': form})
