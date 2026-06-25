from django import forms
from .models import AdmissionApplication

class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ["name", "email", "password"]

        labels = {
            "name": "Enter your Name",
            "email": "Enter your Email",
            "password": "Enter Password"
        }

        widgets = {
            "password": forms.PasswordInput(),
        }

        error_messages = {
            "name": {"required": "Name Can't be empty"},
            "email": {"required": "Email Can't be empty"},
            "password": {"required": "Password Can't be empty"},
        }
        
        help_texts = {
            "name": "Enter Your Full Name.", 
        }

    # Extra validation (optional lekin recommended)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required!")
        return email