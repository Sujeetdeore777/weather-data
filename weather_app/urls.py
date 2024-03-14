# weather_api_project/urls.py
from django.urls import path
from .import views


urlpatterns = [
    path('', views.WeatherDataList, name='weather-data-list'),
    path('Weather', views.Weather, name='Weather'),
    path('WeatherDataShow', views.WeatherDataShow, name='WeatherDataShow'),
]
