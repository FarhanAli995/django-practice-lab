from django.contrib import admin
from .models import AdmissionApplication

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'father_guardian_name', 'class_applied_for', 'contact_number', 'created_at')
    search_fields = ('student_full_name', 'cnic_bform_number', 'contact_number')
    list_filter = ('class_applied_for', 'gender', 'created_at')
