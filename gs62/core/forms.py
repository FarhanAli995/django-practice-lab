from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(widget = forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data.get('name')
        if valname and not valname.isalpha():
            raise forms.ValidationError("Name can only contain letters (no spaces or numbers).")
        return valname

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data