import requests

city = input("Enter your city: ")
api_key = '' # <-- Put your API key here
url_weather = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

response = requests.get(url_weather)

if response.status_code == 200:
    data = response.json()
    temp = data["current"]["temp_c"]
    wind = data["current"]["wind_kph"]
    uv = data["current"]["uv"]
    condition = data["current"]["condition"]["text"]
    print(f"Temperature: {temp}\nWind Speed (Km/h): {wind}\nUV: {uv}\nCondition: {condition}")
else:
    print(f'Error fetching data. Code: {response.status_code}')