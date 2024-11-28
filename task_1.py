import requests
import json

API_key = "482f6f28245b9dee2d19ad54b910a416"

city_name = input("Enter city name: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    weather_info = data["weather"][0]
    temp = data["main"]["temp"]
    print(f"Weather: {weather_info["description"].capitalize()}")
    print(f"Temperature: {temp}")
else:
    print(f"Error: {response.status_code}")