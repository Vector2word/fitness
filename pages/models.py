from django.db import models
from datetime import datetime

class Fitpicture(models.Model):
    fitpicture_title = models.CharField(max_length=255)
    fitpicture_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.fitpicture_title
# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    
    def __str__(self):
        return self.first_name


    
    
    
    
    
    
    
