import requests
import json
from kafka import KafkaProducer

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
api_key = "d4593bcce04eda71196c6bcf156b3eea"
cities_list = ["Paris",'Jerusalem','Meiringen']

weather_data = get_weather_data(api_key, cities_list)

# Save weather data to a JSON file
with open("weather_data.json", "w") as json_file:
    json.dump(weather_data, json_file, indent=4)

print("Weather data saved to weather_data.json")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Send JSON object as a message
message = json.dumps(weather_data).encode('utf-8')
producer.send(topic_name, value=message)

print(message)

# Flush and close the producer
producer.flush()
producer.close()