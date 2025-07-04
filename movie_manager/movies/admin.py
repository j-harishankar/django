from django.contrib import admin
from . models import MovieInfo,CensorInfo,Actor
# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(CensorInfo)
admin.site.register(Actor)
