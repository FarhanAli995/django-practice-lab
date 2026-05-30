from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        initial='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name'
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    email = forms.EmailField(
        max_length=50,
        required=True,
        initial='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email Address'
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    father_name = forms.CharField(
        label='Father name',
        max_length=50,
        required=True,
        initial='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Father Name'
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )
