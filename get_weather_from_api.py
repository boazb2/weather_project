import requests
import json
import pandas as pd
import mysql.connector
import get_cities_from_db as gc

def get_weather_data(api_key, city_list):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = {}

    for city in city_list:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  # Use metric units for temperature
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            city_weather_data = response.json()
            weather_data[city] = city_weather_data
        else:
            print("Error for city {}: {}".format(city, response.status_code))

    return weather_data

# Example usage

# Save weather data to a JSON file
#with open("weather_data.json", "w") as json_file:
#    json.dump(weather_data, json_file, indent=4)



