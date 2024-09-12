# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    humidity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)