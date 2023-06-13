from kafka import KafkaProducer
import json
import get_weather_from_api as weather
import get_cities_from_db as gc

api_key = "d4593bcce04eda71196c6bcf156b3eea"

# Getting the required cities for a user request

cities_list = gc.get_cities_array("SELECT city_name FROM users_cities")

weather_data = weather.get_weather_data(api_key, cities_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Send JSON object as a message
message = json.dumps(weather_data).encode('utf-8')
producer.send(topic_name, value=message)

#print(message)

# Flush and close the producer
producer.flush()
producer.close()