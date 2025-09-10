from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import os
import time
from documentation.logger import Logger
logger = Logger.get_logger()



class Producer:
    def __init__(self):
        kafka_broker = os.getenv("KAFKA_BROKER","localhost:9092")
        while True:
            try:
                self.producer = KafkaProducer(
                    bootstrap_servers=[kafka_broker],
                    value_serializer=lambda x: json.dumps(x).encode('utf-8')
                )
                logger.info("Connected to Kafka!")
                break
            except NoBrokersAvailable:
                logger.error("Kafka broker not ready yet, waiting...")
                time.sleep(3)

    def send_message(self,topic,message):
        logger.info(f"Sending to {topic}: {message}")
        self.producer.send(topic,message)

    def close(self):
        self.producer.flush()
        self.producer.close()





