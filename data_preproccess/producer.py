from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import os
import time

class Producer:
    def __init__(self):
        kafka_broker = os.getenv("KAFKA_BROKER","kafka:9092")
        while True:
            try:
                self.producer = KafkaProducer(
                    bootstrap_servers=[kafka_broker],
                    value_serializer=lambda x: json.dumps(x).encode('utf-8')
                )
                print("Connected to Kafka!")
                break
            except NoBrokersAvailable:
                print("Kafka broker not ready yet, waiting...")
                time.sleep(2)

    def publish_message(self, topic, message):
        print(f"Sending to {topic}: {message}")
        self.producer.send(topic, message)
        self.producer.flush()





