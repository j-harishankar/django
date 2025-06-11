
from . import views
from django.urls import path
urlpatterns = [
    path('',views.create,name='create'),
    path('list/',views.list,name = 'list'),
    path('edit/',views.edit,name = 'edit'),
    path('movie/',views.movie,name = 'movie')


]
