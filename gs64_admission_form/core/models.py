from django.db import models

class AdmissionApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    CLASS_CHOICES = [
        ('9', 'Class 9 (SSC-I)'),
        ('10', 'Class 10 (SSC-II)'),
        ('11', 'Class 11 (HSSC-I)'),
        ('12', 'Class 12 (HSSC-II)'),
    ]

    RELIGION_CHOICES = [
        ('islam', 'Islam'),
        ('christianity', 'Christianity'),
        ('hinduism', 'Hinduism'),
        ('sikhism', 'Sikhism'),
        ('other', 'Other'),
    ]

    # --- Personal Information ---
    student_full_name = models.CharField(max_length=100)
    father_guardian_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # --- Contact Information ---
    contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    residential_address = models.TextField(max_length=300)

    # --- Academic Information ---
    previous_school_name = models.CharField(max_length=150)
    class_applied_for = models.CharField(max_length=2, choices=CLASS_CHOICES)
    previous_class_marks = models.DecimalField(max_digits=5, decimal_places=2)

    # --- Additional Information ---
    cnic_bform_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=50, default='Pakistani')
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    parent_occupation = models.CharField(max_length=100)
    passport_photo = models.ImageField(upload_to='passports/')

    # --- Declaration ---
    declaration = models.BooleanField()
    parent_signature = models.CharField(max_length=100)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_full_name} - Class {self.get_class_applied_for_display()}"
