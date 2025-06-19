
from . import views
from django.urls import path
urlpatterns = [
    path('',views.create,name='create'),
    path('list/',views.list,name = 'list'),
    path('edit/<pk>',views.edit,name = 'edit'),
    path('delete/<pk>',views.delete,name='delete'),
    path('movie/',views.movie,name = 'movie'),
    path('cred/',views.cred,name='cred')


]
