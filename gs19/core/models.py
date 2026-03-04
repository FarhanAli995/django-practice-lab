from django.db import models    

class Students(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    age = models.IntegerField(default=0)


    def __str__(self):
        return self.name



