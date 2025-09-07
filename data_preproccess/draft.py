from pathlib import Path
import datetime
import



dir_path = Path('/Users/petahiam/podcasts')

for file_path in dir_path.iterdir():
    if file_path.is_file():
        file_path.touch()
        try:
            stats = file_path.stat()

            meta_data = {
                'File size':stats.st_size,
                'Last Modified':datetime.datetime.fromtimestamp(stats.st_mtime),
                'Creation Time':datetime.datetime.fromtimestamp(stats.st_ctime),




            }











        # Add your file processing logic here
        elif file_path.is_dir():
            print(f"Processing directory: {file_path}")
            # Recursively process subdirectories if needed
            process_directory_and_files_pathlib(file_path)

process_directory_and_files_pathlib('/path/to/your/directory')

