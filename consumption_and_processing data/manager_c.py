from stt import STT
from mongo_grid import MongoWavStorage
from elastic import ElasticIndex
from logger import Logger
logger = Logger.get_logger()



class STTSaveToElastic:
    def __init__(self):
        self.mongo_storage = MongoWavStorage("mongodb://localhost:27017/",'idf_db')
        self.stt = STT()
        self.elastic_index = ElasticIndex('muazin','http://localhost:9200')

    def run(self):







