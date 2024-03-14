# weather_api/tests.py
from django.test import TestCase
from .models import WeatherData

class WeatherDataModelTestCase(TestCase):
    def test_weather_data_creation(self):
        WeatherData.objects.create(year=2023, jan=5.5, feb=6.2, mar=7.8, apr=10.1, may=13.4, jun=16.5, jul=18.9, aug=18.2, sep=15.6, oct=11.3, nov=7.8, dec=5.9, winter_mean=6.5, spring_mean=10.4, summer_mean=15.1, autumn_mean=10.8, annual_mean=10.7)
        self.assertEqual(WeatherData.objects.count(), 1)
