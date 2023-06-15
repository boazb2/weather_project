from kafka import KafkaConsumer
import json
import pandas as pd
from telegram.ext import Updater
import sentmessage as sm

# Kafka consumer setup
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

try:
    # Consume and process messages
    for message in consumer:
        value_str = message.value.decode('utf-8')
        value_dict = json.loads(value_str)

        
        data = json.loads(value_dict)
        df = pd.json_normalize(data)
        #df = pd.DataFrame([(key, value_dict[key]['main']['feels_like']) for key in value_dict.keys()], columns=['name', 'feels_like'])

        # Call the 'main' function from sentmessage.py
        #sm.main('483699123', '5993334898:AAHCOt1GTVEW3_0FY-wEWmyMvnt71VceloM', df)  # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token

        print(df)
        

          
# Handle any exceptions and ensure consumer is closed
finally:
    consumer.close()
