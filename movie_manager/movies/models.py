from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.title
# If you don’t override this method, Django uses the default string representation provided by Python,
# which looks like:
#<MovieInfo: MovieInfo object (1)>