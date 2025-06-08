
from . import views
from django.urls import path
urlpatterns = [
    path('',views.create),
    path('list/',views.list),
    path('edit/',views.edit),



]
