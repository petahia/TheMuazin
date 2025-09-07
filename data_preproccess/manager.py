from pathlib import Path
import datetime
from producer import Producer

class SendMetaData:
    def __init__(self,path):
        self.path = path
        self.producer = Producer()


    def run(self):
        path_taken = Path(self.path)
        for file_path in path_taken.iterdir():
            if file_path.is_file():
                file_path.touch()
                try:
                    stats = file_path.stat()
                    meta_data = {
                        'File Path': file_path,
                        'File Name': file_path.name,
                        'File Size': stats.st_size,
                        'Last Modified': datetime.datetime.fromtimestamp(stats.st_mtime),
                        'Creation Time': datetime.datetime.fromtimestamp(stats.st_ctime)
                    }
                    self.producer.publish_message('meta_data',meta_data)

                except:
                    print('can not get the meta data from this file')
            elif path_taken.is_dir():
                print(f"Processing directory: {file_path}")
                return self.run()
            # need to add '/' to the function
            elif not any(path_taken.iterdir()):
                return "the directory is empty"




if __name__ == '__main__':
    path = '/Users/petahiam/podcasts'
    d = SendMetaData(path)
    d.run()


