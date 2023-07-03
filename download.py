from office365_api import SharePoint
import re
import sys, os
from pathlib import PurePath
import environ
env = environ.Env()
environ.Env.read_env()

FILE_NAME=env('file_name')
FOLDER_NAME=env('folder_name')

def save_file(file_n, file_obj):
    file_dir_path = PurePath("download", file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

def get_file(file_n, folder):
    print(f"Downloading {file_n} from {folder}...")
    file_obj = SharePoint().download_file(file_n, folder)
    save_file(file_n, file_obj)

def get_files(folder):
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        print(file)
        get_file(file.name, folder)

def get_files_by_pattern(keyword, folder):
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        if re.search(keyword, file.name):
            get_file(file.name, folder)

if __name__ == '__main__':
    get_file(file_n=FILE_NAME, folder=FOLDER_NAME)
    