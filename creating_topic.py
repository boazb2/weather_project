from kafka import KafkaAdminClient
from kafka.admin import NewTopic

def create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor):
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    # Create a NewTopic object with the desired configuration
    topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

    # Create the topic using the admin client
    admin_client.create_topics(new_topics=[topic])

    print(f"Topic '{topic_name}' created successfully.")

# Provide the Kafka cluster configuration
bootstrap_servers = 'cnt7-naya-cdh63:9092'  # Replace with the appropriate bootstrap servers

# Provide the topic details
topic_name = 'weather_topic'
num_partitions = 3
replication_factor = 1

# Call the function to create the topic
create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor)