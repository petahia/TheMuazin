from pathlib import Path
import datetime
from producer import Producer


class ManagerSendMetaData:
    def __init__(self,path):
        self.path = path
        self.producer = Producer()


    def run(self,current_path=None):
        path_taken = Path(self.path)
        if not any(path_taken.iterdir()):
            return "the directory is empty"
        for file_path in path_taken.iterdir():
            if file_path.is_file():
                try:
                    stats = file_path.stat()
                    meta_data = {
                        'File Path': str(file_path),
                        'File Name': file_path.name,
                        'File Size': stats.st_size,
                        'Last Modified': datetime.datetime.fromtimestamp(stats.st_mtime).isoformat(),
                        'Creation Time': datetime.datetime.fromtimestamp(stats.st_ctime).isoformat()
                    }
                    self.producer.send_message('muazin',meta_data)


                except Exception as e:
                    print(f"Error getting metadata from {file_path}: {e}")
            elif path_taken.is_dir():
                print(f"Processing directory: {file_path}")
                return self.run(f"{file_path}/")
        return self.producer.close()


if __name__ == '__main__':
    path = '/Users/petahiam/podcasts'
    d = ManagerSendMetaData(path)
    d.run()


