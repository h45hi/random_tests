""" weather app which print city name,current temperature, min and max temperature of current day"""

import requests

api_address = 'http://openweathermap.org/data/2.5/weather'

city = input('enter city name')

api = 'b6907d289e10d714a6e88b30761fae22'

url = api_address+'?appid='+api+'&q='+city

json_data = requests.get(url).json()

name,temperature,min_temp,max_temp = json_data['name'], json_data['main']['temp'], json_data['main']['temp_min'], json_data['main']['temp_max']

print(f'{name} has {temperature} celcius.Maximum temperature is {max_temp} and minimum temperature is {min_temp}')
