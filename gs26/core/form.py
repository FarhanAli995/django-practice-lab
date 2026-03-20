from django import forms


class StudentsData(forms.Form):
    First_Name = forms.CharField( 
        label='First Name',
        label_suffix=" ",
        initial="Sonam",
        required= False, 
        disabled= True,   
    )




class TeachersData(forms.Form):
    Teacher_Name = forms.CharField(
        label='Teacher Name',
    )