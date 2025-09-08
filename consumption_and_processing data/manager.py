from consumer import Consumer
from mongo import MongoConnect
from elastic import ElasticIndex
from generate_id import IDGenerator

class ManagerSendToMongoElastic:
    def __init__(self):
        self.id_generator = IDGenerator(f"{file_data['name']}_{file_data['size']}_{file_data['creation_date']}")
        self.mongo_connect = MongoConnect("mongodb://localhost:27017/")
        self.elastic_connect = ElasticIndex('muazin','http://localhost:9200')
        self.consume = Consumer('muazin')

    def run(self):
        print("Service started, waiting for messages from Kafka...")
        for message in self.consume.consumer:
            try:
                file_data = message.value
                unique_id = self.id_generator.generate_unique_id(file_data)
                id_and_metadata = {
                    'id':unique_id,
                    'metadata':message.value
                    }

                self.elastic_connect.send_metadata_to_es(file_data, unique_id)


            save_to_mongo(file_data, unique_id)

            print(f"Processed file: {file_data['name']} with ID: {unique_id}")

        except Exception as e:
        print(f"Error processing message: {e}")

def send_metadata_to_es(file_data, unique_id):

    doc = {
        "name": file_data["name"],
        "size": file_data["size"],
        "creation_date": file_data["creation_date"],
        "other_metadata": file_data.get("other_metadata", {})
    }
    es.index(index=ES_INDEX, id=unique_id, document=doc)

def save_to_mongo(file_data, unique_id):

    doc = {
        "_id": unique_id,
        "content": file_data["content"]
    }
    mongo_collection.replace_one({"_id": unique_id}, doc, upsert=True)


