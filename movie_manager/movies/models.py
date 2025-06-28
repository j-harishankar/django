from collections import deque
from django.db import models

# Create your models here.
class director(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
class CensorInfo(models.Model):
    rating = models.CharField(max_length=10)
    certified_by = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.certified_by
class Actor(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='images/',null=True)
    censor = models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directed_by = models.ForeignKey(director,on_delete=models.CASCADE,related_name='directed_movie',null=True)
    actors = models.ManyToManyField(Actor,related_name="actor_movie")
    def __str__(self):
        return self.title
# If you don’t override this method, Django uses the default string representation provided by Python,
# which looks like:
#<MovieInfo: MovieInfo object (1)>