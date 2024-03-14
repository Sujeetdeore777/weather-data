# weather_api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import parse_weather_data
from django.shortcuts import render
from django.core.paginator import Paginator



@api_view(['GET'])
def WeatherDataList(request):
    queryset = WeatherData.objects.all()
    serializer = WeatherDataSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Weather(request):
    url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt'
    weather_data = parse_weather_data(url)
    
    # Save each entry in the parsed data into the database
    for data_entry in weather_data:
        WeatherData.objects.update_or_create(year=data_entry['year'], defaults=data_entry)
    
    return Response({'message': 'Weather data saved to database successfully.'}, status=status.HTTP_201_CREATED)


# def WeatherDataShow(request):
#     weather_data = WeatherData.objects.all()
#     return render(request, 'home.html', {'weather_data': weather_data})

def WeatherDataShow(request):
    weather_data = WeatherData.objects.order_by('-year')  # Order by the 'year' field
    paginator = Paginator(weather_data, 50)  # Show 50 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})