from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'teacher_name', 'email', 'password')
