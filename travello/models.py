from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None)
    desc = models.TextField(max_length=1000)
    price = models.IntegerField()
    offer = models.BooleanField()