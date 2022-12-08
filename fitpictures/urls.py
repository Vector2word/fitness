
from django.urls import path
from . import views



urlpatterns = [
   path('', views.fitpictures, name='fitpictures'),
    
]
