from elasticsearch import Elasticsearch


class ElasticIndex:
    def __init__(self,index_name,connction_string):
        self.es = Elasticsearch(connction_string)
        self.index_name = index_name

    def send_metadata_to_es(self,file_data, unique_id):
        try:
            doc = {
                "name": file_data["File Name"],
                "path":file_data["File Path"],
                "size": file_data["File Size"],
                "creation_date": file_data["Creation Time"],
                "last modified": file_data['Last Modified']

            }
            self.es.index(index=self.index_name, id=unique_id, document=doc)

        except Exception as e:
            print(f"A problem occurred while indexing the data:{e}")






