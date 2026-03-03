from django.db import models

# Create your models here.



class Student(models.Model):
    stuID = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)


 
 