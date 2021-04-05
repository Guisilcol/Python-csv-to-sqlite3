import Config
import modules.File as File
import modules.Reader as Reader
from pathlib import Path
from tabulate import tabulate

tabulate.PRESERVE_WHITESPACE = True

def read_csv_and_load_fwf() -> None:
    config = Config.get_config_dict()
    DIRECTORYS = config['diretorios']
    CSV_INPUT_DIRECTORY = config['diretorios'][0]
    SQLITE_OUTPUT_DIRECTORY = config['diretorios'][1]
    SQLITE_DB_NAME = config['sqliteDbName']
    SQLITE_DB_ABSOLUTE_PATH = '{}/{}'.format(SQLITE_OUTPUT_DIRECTORY, SQLITE_DB_NAME)
    LOG_PATH = config['logFilepath']
    
    if File.check_if_the_folders_are_created(DIRECTORYS):
        print("> As pastas necessárias já estão criadas")
    else:
        File.create_folders(DIRECTORYS)
        print("> As pastas necessárias não foram criadas. O programa fará a criação de todas")
    
    print("> Iniciando processo de transformação")
    
    for directory in File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, '.csv'):
        filename = "{}.csv".format(Path(directory).stem)
        new_filename = "{}.txt".format(Path(directory).stem)
        
        print("> Iniciando o processo do arquivo {} para {}".format(filename, new_filename))
        
        dataframe = Reader.delimited_file_to_dataframe(directory)

        content = tabulate(dataframe.values.tolist(), list(dataframe.columns),
                           tablefmt="plain",
                           colalign=("left", "left"), 
                           stralign="left", 
                           numalign="left",
                           disable_numparse=True)
        
        relative_directory_of_new_filename = "{}/{}".format(SQLITE_OUTPUT_DIRECTORY, new_filename)
        open(relative_directory_of_new_filename, "w", encoding='utf-8') \
            .write(content)
        
        print("> Processamento do arquivo {} concluido".format(new_filename))
        
def read_fwf_and_load_csv() -> None:
    config = Config.get_config_dict()
    DIRECTORYS = config['diretorios']
    CSV_INPUT_DIRECTORY = config['diretorios'][0]
    SQLITE_OUTPUT_DIRECTORY = config['diretorios'][1]
    SQLITE_DB_NAME = config['sqliteDbName']
    SQLITE_DB_ABSOLUTE_PATH = '{}/{}'.format(SQLITE_OUTPUT_DIRECTORY, SQLITE_DB_NAME)
    LOG_PATH = config['logFilepath']
    
    if File.check_if_the_folders_are_created(DIRECTORYS):
        print("> As pastas necessárias já estão criadas")
    else:
        File.create_folders(DIRECTORYS)
        print("> As pastas necessárias não foram criadas. O programa fará a criação de todas")
    
    print("> Iniciando processo de transformação")
    
    for directory in File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, '.txt'):
        filename = "{}.txt".format(Path(directory).stem)
        new_filename = "{}.csv".format(Path(directory).stem)
        
        print("> Iniciando o processo do arquivo {} para {}".format(filename, new_filename))
        
        dataframe = Reader.fixed_width_file_to_dataframe(directory)
        
        delimiter = None
        try:
            parameters = Reader.get_parameters_of_file(directory)
            delimiter = parameters['sep'] if parameters['sep'] != None else ";"
        except:
            delimiter = ";"
        
        relative_directory_of_new_filename = "{}/{}".format(SQLITE_OUTPUT_DIRECTORY, new_filename)
        dataframe.to_csv(relative_directory_of_new_filename, sep=delimiter, index=False)
        
        print("> Processamento do arquivo {} concluido".format(new_filename))
    

    
    
    
    