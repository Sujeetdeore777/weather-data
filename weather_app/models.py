# weather_api/models.py
from django.db import models
from django.utils import timezone


class WeatherData(models.Model):
    year = models.IntegerField(unique=True)
    jan = models.FloatField(null=True, blank=True)
    feb = models.FloatField(null=True, blank=True)
    mar = models.FloatField(null=True, blank=True)
    apr = models.FloatField(null=True, blank=True)
    may = models.FloatField(null=True, blank=True)
    jun = models.FloatField(null=True, blank=True)
    jul = models.FloatField(null=True, blank=True)
    aug = models.FloatField(null=True, blank=True)
    sep = models.FloatField(null=True, blank=True)
    oct = models.FloatField(null=True, blank=True)
    nov = models.FloatField(null=True, blank=True)
    dec = models.FloatField(null=True, blank=True)
    winter_mean = models.FloatField(null=True, blank=True)
    spring_mean = models.FloatField(null=True, blank=True)
    summer_mean = models.FloatField(null=True, blank=True)
    autumn_mean = models.FloatField(null=True, blank=True)
    annual_mean = models.FloatField()
    last_updated = models.DateTimeField(default=timezone.now)  # Set default value

    def __str__(self):
        return str(self.year)
