import json 
import modules.File as File
import modules.Reader as Reader
import modules.Sqlite as Sqlite
import Config
import warnings
from pathlib import Path
import sys

def read_file_and_load_sqlite3() -> None:
    try:
        config = Config.get_config_dict()
        DIRECTORYS = config['diretorios']
        CSV_INPUT_DIRECTORY = config['diretorios'][0]
        SQLITE_OUTPUT_DIRECTORY = config['diretorios'][1]
        SQLITE_DB_NAME = config['sqliteDbName']
        SQLITE_DB_ABSOLUTE_PATH = '{}/{}'.format(SQLITE_OUTPUT_DIRECTORY, SQLITE_DB_NAME)
        LOG_PATH = config['logFilepath']
                     
        print("> Iniciando processo")
        print("> Criando/Acessando o banco de dados")

        database_connection = Sqlite.access_database(SQLITE_DB_ABSOLUTE_PATH)

        print("> Banco de dados conectado")    
        print("> Iniciando processo de exportação")
        
        
        list_of_txt = File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, ".txt")
        list_of_csv = File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, ".csv")
        list_of_files = list_of_csv + list_of_txt
            
        for directory in list_of_files:
            try:
                table_name = Path(directory).stem
                print("> Arquivo '{}' será processado".format(table_name))
                
                if(directory.endswith(".csv")):
                    dataframe = Reader.delimited_file_to_dataframe(directory)
                else: 
                    dataframe = Reader.fixed_width_file_to_dataframe(directory)
                
                Sqlite.load_csv(dataframe, table_name, database_connection)
                print("> Tabela '{}' carregada com sucesso".format(table_name))
                
            except ValueError as e:
                print("> Erro: Pulando o processamento do arquivo '{}'. O nome da tabela informada já existe".format(table_name))
                
            except Exception as e:
                    File.generate_log(LOG_PATH, e)
                    print("> Ocorreu um erro desconhecido durante o processamento do arquivo '{}'".format(table_name))

    except Exception as e:
        File.generate_log(LOG_PATH, e)
        print("> Ocorreu um erro desconhecido durante o processo")

def read_file_and_load_sqlite3_beta() -> None: 
    try:
        config = Config.get_config_dict()
        DIRECTORYS = config['diretorios']
        CSV_INPUT_DIRECTORY = config['diretorios'][0]
        SQLITE_OUTPUT_DIRECTORY = config['diretorios'][1]
        SQLITE_DB_NAME = config['sqliteDbName']
        SQLITE_DB_ABSOLUTE_PATH = '{}/{}'.format(SQLITE_OUTPUT_DIRECTORY, SQLITE_DB_NAME)
        LOG_PATH = config['logFilepath']
                     
        print("> Iniciando processo")
        print("> Criando/Acessando o banco de dados")

        database_connection = Sqlite.access_database(SQLITE_DB_ABSOLUTE_PATH)

        print("> Banco de dados conectado")    
        print("> Iniciando processo de exportação")
        
        
        list_of_txt = File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, ".txt")
        list_of_csv = File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY, ".csv")
        list_of_files = list_of_csv + list_of_txt
            
        for directory in list_of_files:
            try:
                table_name = Path(directory).stem
                print("> Arquivo '{}' será processado".format(table_name))
                
                if(directory.endswith(".csv")):
                    dataframe = Reader.delimited_file_to_dataframe(directory)
                else: 
                    dataframe = Reader.fixed_width_file_to_dataframe(directory)
                
                Sqlite.load_csv(dataframe, table_name, database_connection)
                print("> Tabela '{}' carregada com sucesso".format(table_name))
                
            except ValueError as e:
                print("> Erro: Pulando o processamento do arquivo '{}'. O nome da tabela informada já existe".format(table_name))
                
            except Exception as e:
                    File.generate_log(LOG_PATH, e)
                    print("> Ocorreu um erro desconhecido durante o processamento do arquivo '{}'".format(table_name))

    except Exception as e:
        File.generate_log(LOG_PATH, e)
        print("> Ocorreu um erro desconhecido durante o processo")

def read_file_and_load_sqlserver() -> None: 
    pass

def read_file_and_load_oracle() -> None: 
    pass

def read_file_and_load_mysql() -> None: 
    pass

    