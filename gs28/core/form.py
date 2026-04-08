from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        initial='default value',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'field_id',
                'placeholder': 'Enter value'
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