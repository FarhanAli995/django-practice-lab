from django.db import models

# Create your models here.

class DjangoCourse(models.Model):
    courseName = models.CharField(max_length=70)
    courseFee = models.IntegerField()
    seatsAvailable = models.IntegerField()
    courseID = models.IntegerField()

    def __str__(self):
        return self.courseName