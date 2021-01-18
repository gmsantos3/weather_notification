# this one script is static for the oporto city

import requests
import json
from win10toast import ToastNotifier

f = open('S:/Python/WeatherAp/api_key.txt', 'r')
key = f.read()
api_key = key

city = 'oporto'
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (
    city, api_key)

response = requests.get(url)
weather = dict(json.loads(response.text))


with open('S:/Python/WeatherAp/data.txt', 'w+') as file:
    weather_info = file.write(json.dumps(weather))


def get_weather():
    sky = str(weather['weather'][0]['description'])
    skyUp = sky.capitalize()
    min_temp = str(weather['main']['temp_min'])
    max_temp = str(weather['main']['temp_max'])
    temp = str(weather['main']['temp'])
    feels_temp = str(weather['main']['feels_like'])
    print(sky, min_temp, max_temp, temp, feels_temp)
    a = (skyUp + '\n' +
          'Temp outside is ' + temp + '°C, feels like ' + feels_temp + '°C' + '\n' +
          'Min for today is ' + min_temp + '°C, max is ' + max_temp + '°C')
    print(skyUp + '\n' +
          'Temp outside is ' + temp + '°C, feels like ' + feels_temp + '°C' + '\n' +
          'Min for today is ' + min_temp + '°C, max is ' + max_temp + '°C')
    toast = ToastNotifier()
    toast.show_toast("Weather", a, duration=15)



get_weather()



