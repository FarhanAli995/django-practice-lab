from django import forms


class StudentsData(forms.Form):
    First_Name = forms.CharField( 
        label='First Name',
        label_suffix=" ",
        initial="Sonam",
        required= False, 
        disabled= True,  
        help_text= "Not more than 70 characters",
         
    )




class TeachersData(forms.Form):
    Teacher_Name = forms.CharField(
        widget= forms.Textarea,
        label="Enter Your Name"
    )

    