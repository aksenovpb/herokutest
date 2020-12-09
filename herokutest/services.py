import requests
from django.conf import settings


def get_weather_info():
    token = settings.OPEN_WEATHER_API_TOKEN
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?id=498817&appid={token}&units=metric')
    return response.json()
