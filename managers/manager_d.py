from logics.classification import ContentClassification
from storage.elastic import ElasticIndex

class SendClassifiedToElastic:
    def __init__(self,content):
        self.classifieder = ContentClassification(content)
        self.elastic_index = ElasticIndex('muazin','http://localhost:9200')

    def run(self):
        try:
            for hit in self.elastic_index.retrive_text()["hits"]["hits"]:
                field_text = hit['_source']['field_to_loop']
                self.calculate_danger_percentage(self)

                self.set_criminal_event(self, percentage)

                self.sesegment_danger_levels(self,percentage)


        except Exception as e:
            logger.error(f"Error in STTSaveToElastic pipeline: {e}")






