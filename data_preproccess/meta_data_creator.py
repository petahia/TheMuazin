from pathlib import Path
import datetime

class MetaDataReader:
    def __init__(self,file_path):
        self.file_path = file_path

    def process_directory_and_files_pathlib(self,path):
        path_taken = Path(path)
        if path_taken.is_file():
            path_taken.touch()
            try:
                stats = path_taken.stat()
                meta_data = {
                    'File Path':path_taken,
                    'File Name':path_taken.name,
                    'File Size':stats.st_size,
                    'Last Modified':datetime.datetime.fromtimestamp(stats.st_mtime),
                    'Creation Time':datetime.datetime.fromtimestamp(stats.st_ctime)
                }
                return meta_data
            except:
                print('can not get the meta data from this file')
        elif path_taken.is_dir():
            print(f"Processing directory: {path_taken}")
            return self.process_directory_and_files_pathlib(f"{path_taken}/")
        elif not any(path_taken.iterdir()):
            return "the directory is empty"









































