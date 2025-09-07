from pathlib import Path
import datetime


class SendMetaData:
    def __init__(self,file_path):
        self.file_path = file_path

    def crate_meta_data(self):
        dir_path = Path(self.file_path)
        for file_path in dir_path.iterdir():
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

                    # לשלוח לקפקה בתוך הלולאה
                except:
                    print('can not get the meta data for this file')

            elif file_path.is_dir():
                print(f"Processing directory: {file_path}")
                self.crate_meta_data()




d = SendMetaData('/Users/petahiam/podcasts')


