import requests
from django.shortcuts import render
from .models import WeatherData

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'ec54d833409aa75d4293a952423eb5e3'  # Replace with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        weather_data = response.json()

        # Save data to database
        WeatherData.objects.create(
            city=weather_data['name'],
            temperature=weather_data['main']['temp'],
            description=weather_data['weather'][0]['description'],
            humidity=weather_data['main']['humidity']
        )

        context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity']
        }
        return render(request, 'weather.html', context)
    
    return render(request, 'weather.html')