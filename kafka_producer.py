from kafka import KafkaProducer
import pandas as pd
import json
import get_weather_from_api as weather
import get_cities_from_db as gc

api_key = "d4593bcce04eda71196c6bcf156b3eea"

# Getting the required cities for a user request

cities_list = gc.get_cities_array("SELECT distinct city_name FROM users_cities")
users_cities_df = gc.get_users_cities("SELECT uc.bot_user_id,uc.city_name,u.first_name,u.last_name FROM users_cities uc join users u on uc.bot_user_id = u.bot_user_id")

weather_data = weather.get_weather_data(api_key, cities_list)

weather_data_df  = pd.DataFrame([(key, weather_data[key]['main']['feels_like']) for key in weather_data.keys()], columns=['city_name', 'feels_like'])

merged_df = pd.merge(users_cities_df, weather_data_df, on='city_name', how='inner')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Send JSON object as a message
message = json.dumps(merged_df.to_json(orient='records')).encode('utf-8')
producer.send(topic_name, value=message)


#print(message)
#print(users_cities_df)
#print(weather_data_df)

print(merged_df.to_json(orient='records'))


# Flush and close the producer
producer.flush()
producer.close()