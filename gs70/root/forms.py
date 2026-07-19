from django import forms
from . import models

class Student_Registration(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['student_name','email', 'password']

class Teacher_Registration(Student_Registration):
    class Meta(Student_Registration.Meta):
        fields = ['teacher_name','email', 'password']
