from pymongo import MongoClient
from gridfs import GridFS
from logger import Logger
logger = Logger.get_logger()



class MongoWavStorage:
    def __init__(self,connection_string,db_name):
        self.connect = MongoClient(connection_string)
        self.database = self.connect[db_name]
        self.fs = GridFS(self.database)


    def save_wav(self,file_path,unique_id,file_name):
        try:
            with open(file_path,"rb") as audio_wav:
                file_id = self.fs.put(
                    audio_wav,
                    _id=unique_id,
                    filename=file_name,
                    content_type="audio/wav"
                )
            return file_id

        except Exception as e:
            logger.error(f"Error saving WAV to MongoDB: {e}")
            return None


    def retrieve_wav(self,unique_id):
        try:
            retrieved_file = self.fs.get(unique_id)
            content = retrieved_file.read()
            return content
        except Exception as e:
            logger.error(f"Error retrieving WAV from MongoDB: {e}")

