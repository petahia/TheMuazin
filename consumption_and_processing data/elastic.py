from elasticsearch import Elasticsearch


class ElasticIndex:
    def __init__(self,index_name,connction_string):
        self.es = Elasticsearch(connction_string)
        self.index_name = index_name

    def send_metadata_to_es(self,file_data, unique_id,doc):
        try:
            doc = {
                "name": file_data["name"],
                "size": file_data["size"],
                "creation_date": file_data["creation_date"],
                "other_metadata": file_data.get("other_metadata", {})
            }
            self.es.index(index=ES_INDEX, id=unique_id, document=doc)

        except Exception as e:
            print(f"A problem occurred while indexing the data:{e}")




