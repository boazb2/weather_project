from kafka import KafkaConsumer
from kafka.errors import KafkaError

def is_topic_up(topic, bootstrap_servers):
    try:
        consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
        topics = consumer.topics()
        return topic in topics
    except KafkaError:
        return False

# Usage example
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate broker address
topic_name = 'weather_topic'  # Replace with the name of the topic you want to check

is_up = is_topic_up(topic_name, bootstrap_servers)
if is_up:
    print(f"The topic '{topic_name}' is up.")
else:
    print(f"The topic '{topic_name}' is not available or does not exist.")
