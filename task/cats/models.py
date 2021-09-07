from django.db import models

# Create your models here.

# Model used to store all the details of the cats, this is reflected in our database
class CatDetailModel(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    colour = models.CharField(max_length=40)
    picture = models.ImageField()