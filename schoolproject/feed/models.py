from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=150, blank=False, null=False)



