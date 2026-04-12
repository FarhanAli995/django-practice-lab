from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        initial='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'field_id',
                'placeholder': 'Enter Your Name'
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    Email = forms.EmailField(
        max_length=50,
        required=True,
        initial='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'field_id',
                'placeholder': 'Enter Your Email Address'
            }
        ),
        error_messages={
            'required': 'This field is required',
            'invalid': 'Invalid value'
        }
    )

    Father_name = forms.CharField(
        max_length=50,
        required=True,
        initial='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'field_id',
                'placeholder': 'Enter Your Father Name'
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