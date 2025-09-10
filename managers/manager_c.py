from logics.stt import STT
from storage.mongo_grid import MongoWavStorage
from storage.elastic import ElasticIndex
from logging.logger import Logger
logger = Logger.get_logger()



class STTSaveToElastic:
    def __init__(self):
        self.mongo_storage = MongoWavStorage("mongodb://localhost:27017/",'idf_db')
        self.stt = STT()
        self.elastic_index = ElasticIndex('muazin','http://localhost:9200')

    def run(self):
        try:
            for grid_out in self.mongo_storage.fs.find():
                unique_id = grid_out._id

                content = self.mongo_storage.retrieve_wav(unique_id)

                text = self.stt.record_wav(content)

                self.elastic_index.update_doc(text,unique_id)

        except Exception as e:
            logger.error(f"Error in STTSaveToElastic pipeline: {e}")




if __name__ == '__main__':
    s = STTSaveToElastic()
    s.run()











