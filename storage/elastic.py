from elasticsearch import Elasticsearch
from logger import Logger
logger = Logger.get_logger()



class ElasticIndex:
    def __init__(self,index_name,connection_string):
        self.es = Elasticsearch(connection_string)
        self.index_name = index_name

    def send_metadata_to_es(self,file_data,unique_id):
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
            logger.info(f"A problem occurred while indexing the data:{e}")

    def update_doc(self,text,unique_id):
        try:
            update_body = {
                "doc": {
                    "Text":text
                }
            }
            response = self.es.update(index=self.index_name, id=unique_id, body=update_body)
            return response

        except Exception as e:
            logger.info(f"A problem occurred while updating the data:{e}")


    def retrive_text(self):
        try:
            response = self.es.search(
                index=self.index_name,
                body={
                    "query": {"match_all": {}},
                    "_source": ["Text"]  # Specify the fields to retrieve
                }
            )
            return response

        except Exception as e:
            logger.error(f"Error retrieving document: {e}")




