from django import forms



class StudentsData(forms.Form):
    First_Name = forms.CharField(
        max_length=50,
        required=True,
        initial='Farhan',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter value',
                'id': 'first_name'  
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )
    Last_Name = forms.CharField(
        max_length=50,
        initial='Khan',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter value',
                'id': True
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    Email = forms.EmailField(
        max_length=70,
        required=True,
        initial="alyfarhan4@gmail.com",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email',
                'id': False
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )   


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
class Teachers(forms.Form):
    name = forms.CharField(
        max_length=70,
        required=True,
        initial='default value',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name_id',
                'placeholder': 'Enter Your Name'
            }
        ),
    
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )
    email = forms.EmailField(
        max_length=70,
        required=True,
        initial='default value',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Email_id',
                'placeholder': 'Enter Your Email'
            }
        ),
    
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data