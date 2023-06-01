from kafka import KafkaConsumer, KafkaAdminClient
from kafka.errors import KafkaTimeoutError

def is_kafka_up():
    bootstrap_servers = 'localhost:9092'  # Update with the bootstrap servers of your Kafka cluster
    topic = '__some_topic__'  # Replace with a topic that exists in your Kafka cluster

    try:
        # Create a KafkaConsumer to connect to Kafka
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=None,  # Avoid consuming from any existing consumer group
            auto_offset_reset='earliest',  # Start consuming from the beginning of the topic
            enable_auto_commit=False,  # Disable automatic offset committing
            consumer_timeout_ms=5000  # Timeout for the consumer to avoid waiting indefinitely
        )

        # Check if the Kafka topic exists
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
        topic_metadata = admin_client.describe_topics(topic)
        topic_exists = len(topic_metadata.topics) == 1

        return topic_exists

    except KafkaTimeoutError:
        return False

# Call the function to check Kafka connectivity
kafka_up = is_kafka_up()
print("Kafka is up" if kafka_up else "Kafka is down")

--create --topic weather_topic --bootstrap-server <bootstrap_servers> --partitions <num_partitions> --replication-factor <replication_factor>