from kafka import KafkaConsumer

# Kafka consumer setup
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the Kafka topic

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Consume and print messages
for message in consumer:
    # Decode and print the message value as string
    print(message.value.decode('utf-8'))

# Close the consumer
consumer.close()
