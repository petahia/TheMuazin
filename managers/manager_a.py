from pathlib import Path
import datetime
from streaming.producer import Producer
from logger import Logger
logger = Logger.get_logger()



class PreProccess:
    def __init__(self,path):
        self.path = path
        self.producer = Producer()


    def run(self,current_path=None):
        logger.info("Service started")
        path_taken = Path(self.path)
        if not any(path_taken.iterdir()):
            return logger.info("the directory is empty")
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
                    logger.error(f"Error getting metadata from {file_path}: {e}")
            elif path_taken.is_dir():
                logger.info(f"Processing directory: {file_path}")
                return self.run(f"{file_path}/")
        return self.producer.close()


if __name__ == '__main__':
    path = '/Users/petahiam/podcasts'
    d = PreProccess(path)
    d.run()


