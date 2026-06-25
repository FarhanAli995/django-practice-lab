from django.contrib import admin

from .models import AdmissionApplication


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")

