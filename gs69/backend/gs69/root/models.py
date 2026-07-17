from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    education = models.CharField(max_length=100)
    
    # Professional Information
    profession = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']