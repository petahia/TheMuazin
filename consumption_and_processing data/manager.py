from consumer import Consumer
from mongo import MongoWavStorage
from elastic import ElasticIndex
from generate_id import IDGenerator

class ManagerSendToMongoElastic:
    def __init__(self):
        self.consume = Consumer('muazin')
        self.id_generator = IDGenerator(['File Name','File Size','Creation Time'])
        self.mongo_storage = MongoWavStorage("mongodb://localhost:27017/",'idf_db')
        self.elastic_index = ElasticIndex('muazin','http://localhost:9200')


    def run(self):
        print("Service started, waiting for messages from Kafka...")
        for message in self.consume.consumer:
            try:
                file_data = message.value
                unique_id = self.id_generator.generate_unique_id(file_data)
                file_path = file_data['File Path']

                self.mongo_storage.save_wav(file_path,unique_id,file_data['File Name'])

                self.elastic_index.send_metadata_to_es(file_data, unique_id)

                print(f"Processed file: {file_data['name']} with ID: {unique_id}")

            except Exception as e:
                print(f"Error processing message: {e}")



if __name__ == '__main__':
    m = ManagerSendToMongoElastic()
    m.run()



