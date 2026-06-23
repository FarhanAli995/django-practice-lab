from django import forms

class loginform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data.get('name')
        valemail = cleaned_data.get('email')
        valpassword = cleaned_data.get('password')
        
        if valname and not valname.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters (no numbers or special characters).")
        elif valpassword == "admin":
            raise forms.ValidationError("Password cannot be admin")
        elif valemail == "test@test.com":
            raise forms.ValidationError("Email cannot be test@test.com")
        
        return cleaned_data