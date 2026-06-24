# forms.py
from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date


class AdmissionApplicationForm(forms.Form):
    """
    Student Admission Application Form
    Aga Khan Higher Secondary School, Rahimabad
    """

    # --- Personal Information ---
    student_full_name = forms.CharField(
        label="Student's Full Name",
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Name must contain only letters and spaces.'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'As per official documents',
            'class': 'form-control'
        })
    )

    father_guardian_name = forms.CharField(
        label="Father's/Guardian's Name",
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Name must contain only letters and spaces.'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Parent or legal guardian name',
            'class': 'form-control'
        })
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    GENDER_CHOICES = [
        ('', '-- Select Gender --'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # --- Contact Information ---
    contact_number = forms.CharField(
        label="Contact Number",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{10,15}$',
                message='Enter a valid phone number (10-15 digits).'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., +923001234567',
            'class': 'form-control'
        })
    )

    emergency_contact = forms.CharField(
        label="Emergency Contact",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{10,15}$',
                message='Enter a valid emergency phone number (10-15 digits).'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Alternate relative phone number',
            'class': 'form-control'
        })
    )

    residential_address = forms.CharField(
        label="Residential Address",
        max_length=300,
        widget=forms.Textarea(attrs={
            'placeholder': 'Complete home address with landmark',
            'rows': 3,
            'class': 'form-control'
        })
    )

    # --- Academic Information ---
    previous_school_name = forms.CharField(
        label="Previous School Name",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last institution attended',
            'class': 'form-control'
        })
    )

    CLASS_CHOICES = [
        ('', '-- Select Class --'),
        ('9', 'Class 9 (SSC-I)'),
        ('10', 'Class 10 (SSC-II)'),
        ('11', 'Class 11 (HSSC-I)'),
        ('12', 'Class 12 (HSSC-II)'),
    ]
    class_applied_for = forms.ChoiceField(
        label="Class Applied For",
        choices=CLASS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    previous_class_marks = forms.DecimalField(
        label="Previous Class Marks/Percentage",
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00, 'Marks cannot be less than 0%.'),
            MaxValueValidator(100.00, 'Marks cannot exceed 100%.')
        ],
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g., 85.50',
            'class': 'form-control',
            'step': '0.01'
        })
    )

    # --- Additional Information ---
    cnic_bform_number = forms.CharField(
        label="CNIC / B-Form Number",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{5}-?\d{7}-?\d{1}$|^\d{13}$',
                message='Enter a valid CNIC (xxxxx-xxxxxxx-x) or B-Form number (13 digits).'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., 35201-1234567-1',
            'class': 'form-control'
        })
    )

    nationality = forms.CharField(
        label="Nationality",
        max_length=50,
        initial='Pakistani',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    RELIGION_CHOICES = [
        ('', '-- Select Religion --'),
        ('islam', 'Islam'),
        ('christianity', 'Christianity'),
        ('hinduism', 'Hinduism'),
        ('sikhism', 'Sikhism'),
        ('other', 'Other'),
    ]
    religion = forms.ChoiceField(
        label="Religion",
        choices=RELIGION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    parent_occupation = forms.CharField(
        label="Parent's Occupation",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': "Guardian's profession and workplace",
            'class': 'form-control'
        })
    )

    passport_photo = forms.ImageField(
        label="Passport-size Photo",
        required=True,
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
            'class': 'form-control'
        })
    )

    # --- Declaration ---
    declaration = forms.BooleanField(
        label="I hereby declare that all the information provided above is true and correct to the best of my knowledge. I understand that any false information may result in cancellation of admission.",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    parent_signature = forms.CharField(
        label="Parent/Guardian Signature (Type Full Name)",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # ============================
    # CLEAN METHODS (Validation)
    # ============================

    def clean_student_full_name(self):
        """Clean and validate student's full name."""
        name = self.cleaned_data.get('student_full_name')
        if name:
            name = ' '.join(name.split())  # Remove extra spaces
            if len(name) < 3:
                raise ValidationError("Name must be at least 3 characters long.")
        return name.title()

    def clean_father_guardian_name(self):
        """Clean and validate father's/guardian's name."""
        name = self.cleaned_data.get('father_guardian_name')
        if name:
            name = ' '.join(name.split())
            if len(name) < 3:
                raise ValidationError("Guardian name must be at least 3 characters long.")
        return name.title()

    def clean_date_of_birth(self):
        """Validate date of birth (must be at least 12 years old, not in future)."""
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            if dob > today:
                raise ValidationError("Date of birth cannot be in the future.")
            if age < 12:
                raise ValidationError("Student must be at least 12 years old for higher secondary admission.")
            if age > 25:
                raise ValidationError("Age exceeds the maximum limit for admission.")
        return dob

    def clean_contact_number(self):
        """Clean and validate contact number."""
        phone = self.cleaned_data.get('contact_number')
        if phone:
            phone = phone.replace('-', '').replace(' ', '')
            if not phone.startswith('+92') and not phone.startswith('03'):
                raise ValidationError("Please enter a valid Pakistani phone number (starting with +92 or 03).")
        return phone

    def clean_emergency_contact(self):
        """Clean and validate emergency contact."""
        phone = self.cleaned_data.get('emergency_contact')
        if phone:
            phone = phone.replace('-', '').replace(' ', '')
            if not phone.startswith('+92') and not phone.startswith('03'):
                raise ValidationError("Please enter a valid Pakistani phone number (starting with +92 or 03).")
        return phone

    def clean(self):
        """Cross-field validation."""
        cleaned_data = super().clean()

        contact = cleaned_data.get('contact_number')
        emergency = cleaned_data.get('emergency_contact')

        # Ensure contact and emergency numbers are different
        if contact and emergency and contact == emergency:
            self.add_error('emergency_contact', "Emergency contact must be different from the primary contact number.")

        # Validate photo size
        photo = cleaned_data.get('passport_photo')
        if photo:
            if photo.size > 2 * 1024 * 1024:  # 2MB limit
                self.add_error('passport_photo', "Photo size must not exceed 2MB.")

            valid_types = ['image/jpeg', 'image/png', 'image/jpg']
            if hasattr(photo, 'content_type') and photo.content_type not in valid_types:
                self.add_error('passport_photo', "Only JPEG and PNG images are allowed.")

        return cleaned_data

    def clean_cnic_bform_number(self):
        """Format and validate CNIC/B-Form number."""
        cnic = self.cleaned_data.get('cnic_bform_number')
        if cnic:
            cnic = cnic.replace('-', '').replace(' ', '')
            if len(cnic) == 13:
                # Format as xxxxx-xxxxxxx-x
                cnic = f"{cnic[:5]}-{cnic[5:12]}-{cnic[12]}"
            elif len(cnic) != 15:
                raise ValidationError("CNIC/B-Form number must be 13 digits.")
        return cnic

    def clean_previous_class_marks(self):
        """Validate previous class marks."""
        marks = self.cleaned_data.get('previous_class_marks')
        if marks is not None:
            if marks < 33:
                raise ValidationError("Minimum 33% marks required for admission.")
        return marks

    def clean_parent_signature(self):
        """Validate parent signature matches guardian name."""
        signature = self.cleaned_data.get('parent_signature')
        guardian_name = self.cleaned_data.get('father_guardian_name', '')

        if signature and guardian_name:
            sig_clean = signature.strip().lower().replace(' ', '')
            guardian_clean = guardian_name.strip().lower().replace(' ', '')
            if sig_clean != guardian_clean:
                raise ValidationError("Signature must match the Father's/Guardian's Name exactly.")
        return signature