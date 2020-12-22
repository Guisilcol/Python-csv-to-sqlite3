import json 
import modules.File as File
import modules.Reader as Reader
import modules.Sqlite as Sqlite
import Config
import warnings
from pathlib import Path
import sys

def read_csv_and_load_sqlite3() -> None:
    try:
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
            
        print("> Iniciando processo")
        print("> Criando/Acessando o banco de dados")

        database_connection = Sqlite.access_database(SQLITE_DB_ABSOLUTE_PATH)

        print("> Banco de dados conectado")    
        print("> Iniciando processo de exportação")
            
        for directory in File.get_absolute_directory_of_files(CSV_INPUT_DIRECTORY):
            try:
                table_name = Path(directory).stem
                print("> Arquivo '{}' será processado".format(table_name))
                dataframe = Reader.delimited_file_to_dataframe(directory)
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

    finally:
        print("> Fim do processo")
        input("> Aperte Enter para continuar...")

