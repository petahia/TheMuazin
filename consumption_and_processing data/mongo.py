from pymongo import MongoClient
from gridfs import GridFS



class MongoConnect:
    def __init__(self,connection_string):
        self.connect = MongoClient(connection_string)
        self.database = self.connect['idf_db']
        self.collection = self.database['muazin_records']
        self.fs = GridFS(self.database)

    try:
        # 3. Open the WAV file in binary read mode
        with open(file_path, 'rb') as audio_file:
            # 4. Store the file using GridFS
            file_id = fs.put(audio_file, filename='my_audio.wav', content_type='audio/wav')
            print(f"WAV file '{file_path}' saved to MongoDB with ID: {file_id}")

    except FileNotFoundError:
        print(f"Error: WAV file not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


    def insert(self,document):
        try:
            self.collection.insert_one(document)
            return 'Document was successfully inserted'
        except Exception as e:
            print(f'An error occurred during insertion: {e}')


