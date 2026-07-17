from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import re
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    # Additional fields for validation
    confirm_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm email address'
        }),
        label='Confirm Email',
        help_text='Re-enter your email address to confirm'
    )
    
    class Meta:
        model = UserProfile
        fields = '__all__'  # Includes ALL model fields
        
        # Custom widgets for better UI
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number',
                'required': 'required'
            }),
            'education': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter highest education',
                'required': 'required'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter profession'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 50,
                'placeholder': '0'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
        # Labels for better readability
        labels = {
            'name': 'Full Name',
            'mobile_number': 'Mobile Number',
            'experience_years': 'Years of Experience',
            'is_active': 'Active Status',
        }
        
        # Help texts
        help_texts = {
            'email': 'We\'ll never share your email with anyone else.',
            'experience_years': 'Enter total years of professional experience (0-50).',
        }
        
        # Error messages
        error_messages = {
            'name': {
                'required': 'Full name is required.',
                'max_length': 'Name cannot exceed 100 characters.',
            },
            'email': {
                'invalid': 'Please enter a valid email address.',
                'max_length': 'Email cannot exceed 254 characters.',
            },
            'mobile_number': {
                'required': 'Mobile number is required.',
                'max_length': 'Mobile number cannot exceed 15 characters.',
            },
            'education': {
                'required': 'Education field is required.',
                'max_length': 'Education cannot exceed 100 characters.',
            },
            'experience_years': {
                'min_value': 'Experience years cannot be negative.',
                'max_value': 'Experience years cannot exceed 50.',
            },
        }
    
    def clean_name(self):
        """Validate name: only letters, spaces, dots, and hyphens allowed"""
        name = self.cleaned_data.get('name')
        if name:
            # Remove extra spaces
            name = ' '.join(name.split())
            
            # Check for minimum length
            if len(name) < 2:
                raise ValidationError('Name must be at least 2 characters long.')
            
            # Allow only letters, spaces, dots, hyphens, and apostrophes
            if not re.match(r"^[a-zA-Z\s\.\-']+$", name):
                raise ValidationError(
                    'Name can only contain letters, spaces, dots, hyphens, and apostrophes.'
                )
            
            # Capitalize each word
            name = ' '.join(word.capitalize() for word in name.split())
            
        return name
    
    def clean_email(self):
        """Validate email: check format and uniqueness"""
        email = self.cleaned_data.get('email')
        if email:
            # Check if email is already taken by another profile
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                # Update case: exclude current instance
                if UserProfile.objects.filter(email=email).exclude(pk=instance.pk).exists():
                    raise ValidationError('This email is already registered with another profile.')
            else:
                # Create case: check if email exists
                if UserProfile.objects.filter(email=email).exists():
                    raise ValidationError('This email is already registered.')
            
            # Validate email domain (optional)
            if not any(domain in email.lower() for domain in ['.com', '.org', '.net', '.edu', '.gov']):
                raise ValidationError('Please use a valid email domain (e.g., .com, .org, .net).')
        
        return email
    
    def clean_mobile_number(self):
        """Validate mobile number: digits only, proper format"""
        mobile = self.cleaned_data.get('mobile_number')
        if mobile:
            # Remove spaces, hyphens, and parentheses
            mobile = re.sub(r'[\s\-\(\)]', '', mobile)
            
            # Check if it contains only digits
            if not mobile.isdigit():
                raise ValidationError('Mobile number can only contain digits.')
            
            # Check length
            if len(mobile) < 10:
                raise ValidationError('Mobile number must be at least 10 digits.')
            
            if len(mobile) > 15:
                raise ValidationError('Mobile number cannot exceed 15 digits.')
            
            # Check for common invalid patterns
            if mobile in ['0000000000', '1111111111', '2222222222', '3333333333', 
                         '4444444444', '5555555555', '6666666666', '7777777777',
                         '8888888888', '9999999999', '1234567890', '0987654321']:
                raise ValidationError('Please enter a valid mobile number.')
        
        return mobile
    
    def clean_education(self):
        """Validate education: capitalize properly"""
        education = self.cleaned_data.get('education')
        if education:
            # Remove extra spaces
            education = ' '.join(education.split())
            
            if len(education) < 2:
                raise ValidationError('Education must be at least 2 characters long.')
            
            # Capitalize each word
            education = ' '.join(word.capitalize() for word in education.split())
        
        return education
    
    def clean_profession(self):
        """Validate profession: capitalize properly"""
        profession = self.cleaned_data.get('profession')
        if profession:
            # Remove extra spaces
            profession = ' '.join(profession.split())
            
            if len(profession) < 2:
                raise ValidationError('Profession must be at least 2 characters long.')
            
            # Capitalize each word
            profession = ' '.join(word.capitalize() for word in profession.split())
        
        return profession
    
    def clean_company(self):
        """Validate company: capitalize properly"""
        company = self.cleaned_data.get('company')
        if company:
            # Remove extra spaces
            company = ' '.join(company.split())
            
            if len(company) < 2:
                raise ValidationError('Company name must be at least 2 characters long.')
            
            # Capitalize each word
            company = ' '.join(word.capitalize() for word in company.split())
        
        return company
    
    def clean_experience_years(self):
        """Validate experience years: between 0 and 50"""
        years = self.cleaned_data.get('experience_years')
        if years is not None:
            if years < 0:
                raise ValidationError('Experience years cannot be negative.')
            if years > 50:
                raise ValidationError('Experience years cannot exceed 50.')
            # Convert to integer if it's a float
            if isinstance(years, float):
                if not years.is_integer():
                    raise ValidationError('Experience years must be a whole number.')
                years = int(years)
        
        return years
    
    def clean(self):
        """Cross-field validation"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        name = cleaned_data.get('name')
        profession = cleaned_data.get('profession')
        experience_years = cleaned_data.get('experience_years')
        
        # Validate email confirmation (only if email is provided)
        if email and confirm_email:
            if email != confirm_email:
                self.add_error('confirm_email', 'Email addresses do not match.')
        elif email and not confirm_email:
            self.add_error('confirm_email', 'Please confirm your email address.')
        
        # Validate that experience years match profession
        if experience_years and profession:
            if experience_years > 0 and not profession:
                self.add_error('profession', 'Please specify your profession if you have experience.')
            elif experience_years == 0 and profession:
                # This is fine, just a caution
                pass
        
        # Validate name and email combination
        if name and email:
            # Check if email contains name parts (optional validation)
            name_parts = name.lower().split()
            email_local = email.lower().split('@')[0]
            # This is just a suggestion, not a hard rule
            if not any(part in email_local for part in name_parts):
                # Don't raise error, just add a warning
                pass
        
        return cleaned_data
