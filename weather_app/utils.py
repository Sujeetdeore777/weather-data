# weather_api/utils.py
import requests
from datetime import datetime

def parse_weather_data(url):
    response = requests.get(url)
    lines = response.text.split('\n')
    data = []
    for line in lines[2:]:  # Start from the second line
        values = line.split()
        if not values or not values[0].isdigit() or len(values) < 18:  # Skip invalid lines
            continue
        year = int(values[0])
        monthly_temperatures = [float(val) if val != '---' else None for val in values[1:13]]
        seasonal_means = [float(val) if val != '---' else None for val in values[13:17]]
        annual_mean = float(values[17])
        data.append({
            'year': year,
            'jan': monthly_temperatures[0],
            'feb': monthly_temperatures[1],
            'mar': monthly_temperatures[2],
            'apr': monthly_temperatures[3],
            'may': monthly_temperatures[4],
            'jun': monthly_temperatures[5],
            'jul': monthly_temperatures[6],
            'aug': monthly_temperatures[7],
            'sep': monthly_temperatures[8],
            'oct': monthly_temperatures[9],
            'nov': monthly_temperatures[10],
            'dec': monthly_temperatures[11],
            'winter_mean': seasonal_means[0],
            'spring_mean': seasonal_means[1],
            'summer_mean': seasonal_means[2],
            'autumn_mean': seasonal_means[3],
            'annual_mean': annual_mean,
            'last_updated': datetime.now(),
        })
    return data
