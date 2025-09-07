from kafka import KafkaProducer
import json

from data_preproccess.draft import meta_data

# Initialize KafkaProducer with Kafka broker details
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize messages to JSON
)

# Send a message to a topic
topic_name = 'meta data'
message_data = meta_data
producer.send(topic_name, message_data)

# Ensure all messages are sent before closing
producer.flush()
print(f"Message sent to topic: {topic_name}")