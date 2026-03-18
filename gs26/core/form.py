from django import forms


class StudentsData(forms.Form):
    First_Name = forms.CharField( 
        label='First Name',
    )




class TeachersData(forms.Form):
    Teacher_Name = forms.CharField(
        label='Teacher Name',
    )