import json
import controller.FileToDatabase as FileToDatabase
import warnings
import Config

if __name__ == "__main__":    
    config = Config.get_config_dict()
    IS_IN_DEVELOPMENT = config['isInDevelopment']

    if not IS_IN_DEVELOPMENT:
        warnings.filterwarnings('ignore')           
    
    welcome_message = \
        "       ********** CSV to SQLITE3 ********** \n\n" \
        "1 - Exportar dados de arquivos para banco de dados \n" \
        "2 - Transformar arquivos .csv em arquivos posicionais \n" \
        "3 - Transformar arquivos posicionais em arquivos .csv \n"

    print(welcome_message)
        
    option = input("\n")
    
    if(option == "1"):
        FileToDatabase.read_csv_and_load_sqlite3()
    

    
    