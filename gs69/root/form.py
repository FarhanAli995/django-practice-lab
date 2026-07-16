from django import forms
from django.core import validators
from .model import User

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ['name', "email", "password"]


