from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_Number = forms.IntegerField()
    Reg_Number =forms.IntegerField()

