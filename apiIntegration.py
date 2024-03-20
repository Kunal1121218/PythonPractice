import json
import requests

city_name = input('enter city name')
api_key = '7e6d9286568545ff7ac43bba52f8566b'
api_url =f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'


get_server_information = requests.get(api_url)
data = get_server_information.json()
print(data)

