from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_Number = forms.IntegerField()
    Reg_Number =forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class TeacherRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_Number = forms.IntegerField()
    Reg_Number =forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

