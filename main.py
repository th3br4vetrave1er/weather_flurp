import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('WEATHER_API')

print(
    'Hello there, traveler!'
)
city: str = input('In what city you wanna know weather?: ')

response = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
)

weather_data = response.json()

# the cycle is for us, to understand what data we got with response,
# and we want to see
# for key in weather_data:
#     print(key, ':', weather_data[key])

print(f'So weather in {city}, huh? Ok, let us look at intel I got.')

print(
    f'Looks like we have {weather_data['weather'][0]['description']}.'
    f' And the temperature is {weather_data['main']['temp']} F.'
)

# TODO Add error handling, and let the user decide what info to display