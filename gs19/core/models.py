from django.db import models

# Create your models here.

# class Students(models.Model):
    
#     stuid = models.IntegerField(primary_key=True)
#     stuname = models.CharField(max_length=70)
#     stumail = models.CharField(max_length=70)
#     stupass = models.CharField(max_length=70)
#     comment = models.CharField(max_length=50, default="Not Commented")
    

class Students(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    age = models.IntegerField(default=0)




