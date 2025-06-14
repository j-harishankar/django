from django.forms import ModelForm
from . models import MovieInfo

class MovieForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'#you can also declare specific fields using list refer docs 