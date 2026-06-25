from django.db import models

class AdmissionApplication(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.name}, {self.email}"