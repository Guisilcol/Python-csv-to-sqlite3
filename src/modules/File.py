import os
import re

def check_if_the_folders_are_created(list_of_folders: list) -> bool: 
    for diretory in list_of_folders:
        if not os.path.isdir(diretory):
            return False
    return True

def create_folders(list_of_folders: list) -> None:
    for diretory in list_of_folders:
        os.mkdir(diretory)
        
def get_absolute_directory_of_files(folder_directory: str) -> list:
    file_list = [os.path.join(folder_directory, f) for f in os.listdir(folder_directory) if os.path.isfile(os.path.join(folder_directory, f))]
    return [f for f in file_list if f.endswith('.csv')]

def get_filename_of_absolute_path(directory: str) -> str:
    return re.sub(".+[\\\/]", '', directory)

def generate_log(directory: str, exception: Exception) -> None: 
    separator = '****************************************************************'
    content = """
    {}
    Tipo: {}
    {}
    {}
    """.format(separator, type(exception), exception, separator)
    with open(directory, 'a') as f:
        f.write(content)
