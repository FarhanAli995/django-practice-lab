from django import forms
from django.core import validators

class RegistrationForm(forms.Form):
    # Name max 20 letters ka ho aur sirf letters hon (no numbers)
    username = forms.CharField(
        validators=[
            validators.MaxLengthValidator(20),
            validators.RegexValidator(regex=r'^[a-zA-Z]+$', message="Sirf letters allowed hain!")
        ]
    )
    
    # Age 18 se 60 ke darmiyan ho
    age = forms.IntegerField(
        validators=[
            validators.MinValueValidator(18),
            validators.MaxValueValidator(60)
        ]
    )
    
    # Sirf PDF upload ho sake
    resume = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])]
    )