from logics import ContentClassification
from elastic import ElasticIndex

class SendClassifiedToElastic:
    def __init__(self,content):
        self.classifieder = ContentClassification(content)
        self.elastic_index = ElasticIndex('muazin','http://localhost:9200')

    def run(self):
        try:




        except Exception as e:
            logger.error(f"Error in STTSaveToElastic pipeline: {e}")






