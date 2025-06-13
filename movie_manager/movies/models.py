from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()