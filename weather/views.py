import os

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class WeatherView(View):
    @method_decorator(cache_page(60 * 30))  # Кэширование на 30 минут
    def get(self, request):
        city_name = request.GET.get('city')
        if not city_name:
            return JsonResponse({'error': 'Название города обязательно к заполнению'}, status=400)

        api_key = os.environ.get("API_KEY")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        try:
            response = requests.get(url)
            data = response.json()

            temperature_celsius = data['main']['temp'] - 273.15
            pressure_mm_hg = data['main']['pressure'] * 0.75006375541921
            wind_speed_m_s = data['wind']['speed']

            result = {
                'temperature': round(temperature_celsius, 2),
                'pressure': round(pressure_mm_hg, 2),
                'wind_speed': round(wind_speed_m_s, 2),
            }
            return JsonResponse(result)
        except requests.RequestException as e:
            return JsonResponse({'error': f'Ошибка соединения с OpenWeatherMap: {e}'}, status=500)
