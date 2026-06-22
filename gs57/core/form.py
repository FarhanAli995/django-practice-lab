from django import forms


class CustomerForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.CharField(max_length=15)
    address=forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        val_name = self.cleaned_data["name"]
        
        # 1. Check for minimum length
        if len(val_name) < 4:
            raise forms.ValidationError("Name must be at least 4 characters long.")
            
        # 2. Check if the string contains ONLY letters (no numbers, spaces, or punctuation)
        if not val_name.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters (no numbers or special characters).")
            
        return val_name
    

    