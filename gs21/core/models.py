from django.db import models

# Create your models here.

class Student(models.Model):
    stuID = models.IntegerField(primary_key=True)
    stuName = models.CharField(max_length=70)
    stuEmail = models.EmailField( max_length=70)
    stuPass = models.CharField(max_length=70)

def __str__(self):
    return self.stuName
 
   
 