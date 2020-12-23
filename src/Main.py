import controller.FileToDatabase as FileToDatabase
import controller.FileToFile as FileToFile
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
        
    option = input("Informe a opção: ")
    
    if(option == "1"):
        FileToDatabase.read_file_and_load_sqlite3()
    if(option == "2"):
        FileToFile.read_csv_and_load_fwf()
    if(option == "3"):
        FileToFile.read_fwf_and_load_csv()
    
    print("> Fim do processo")
    input("> Aperte Enter para continuar...")

    
    