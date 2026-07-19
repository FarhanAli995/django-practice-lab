from django.shortcuts import render, redirect
from django.views import View
from . import forms

# Create your views here.


def student_success_page(request):
    return render(request, 'root/student_success.html')


def teacher_success_page(request):
    return render(request, 'root/teacher_success.html')


class StudentFormView(View):
    template_name = 'root/student.html'
    form_class = forms.Student_Registration

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('root:student_success')
        return render(request, self.template_name, {'form': form})


class TeacherFormView(View):
    template_name = 'root/teacher.html'
    form_class = forms.Teacher_Registration

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('root:teacher_success')
        return render(request, self.template_name, {'form': form})