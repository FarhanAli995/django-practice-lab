from django.db import models

# Create your models here.

class Menucatagory(models.Model):
    ID = models.IntegerField(primary_key=True)
    dishname = models.CharField(max_length=70)
    dishdescription = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dishimage = models.ImageField( upload_to="dishimages", height_field=None, width_field=None, max_length=None)
    isavailable = models.BooleanField()



