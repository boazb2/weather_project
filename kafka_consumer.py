from kafka import KafkaConsumer
import json
import pandas as pd
from telegram.ext import Updater

# Kafka consumer setup
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Consume and print messages
for message in consumer:
    # Decode and print the message value as string
    #print(message.value.decode('utf-8'))


    value_str = message.value.decode('utf-8')

    # Parse the JSON string to a Python object
    value_dict = json.loads(value_str)

    df = pd.DataFrame([(key, value_dict[key]['main']['feels_like']) for key in value_dict.keys()], columns=['name', 'feels_like'])
    print(df)

################################################################




################################################################
# Close the consumer
consumer.close()
