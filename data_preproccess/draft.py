from pathlib import Path
import datetime



def process_directory_and_files_pathlib(file_path):
    dir_path = Path(file_path)

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            file_path.touch()
            try:
                stats = file_path.stat()
                meta_data = {
                    'File Path':file_path,
                    'File Name':file_path.name,
                    'File Size':stats.st_size,
                    'Last Modified':datetime.datetime.fromtimestamp(stats.st_mtime),
                    'Creation Time':datetime.datetime.fromtimestamp(stats.st_ctime)
                }
                # לשלוח לקפקה בתוך הלולאה

            except:
                print('can not get the meta data for this file')

        elif file_path.is_dir():
            print(f"Processing directory: {file_path}")
            process_directory_and_files_pathlib(file_path)





process_directory_and_files_pathlib('/Users/petahiam/podcasts')






































