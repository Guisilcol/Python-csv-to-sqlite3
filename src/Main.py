import controller.FileToDatabase as FileToDatabase
import controller.FileToFile as FileToFile
import warnings
import Config
import modules.File as File

if __name__ == "__main__":    
    config = Config.get_config_dict()
    IS_IN_DEVELOPMENT = config['isInDevelopment']

    if not IS_IN_DEVELOPMENT:
        warnings.filterwarnings('ignore')           
    
    if not File.check_if_the_folders_are_created(config['diretorios']):
        print("\n")
        print("> As pastas necessárias não foram criadas. O programa fará a criação de todas")
        File.create_folders(config['diretorios'])
        print("> As pastas foram criadas com sucesso")
    
    welcome_message = \
        "\n\n       ********** CSV to SQLITE3 ********** \n\n" \
        "1 - Exportar dados de arquivos para banco de dados SQLITE3 \n" \
        "2 - Transformar arquivos .csv em arquivos posicionais \n" \
        "3 - Transformar arquivos posicionais em arquivos .csv \n" \
        "4 - Exportar os arquivos em tabelas SQLSERVER - NÃO IMPLEMENTADO\n" \
        "5 - Exportar os arquivos em tabelas ORACLE - NÃO IMPLEMENTADO\n" \
        "6 - Exportar os arquivos em tabelas MYSQL - NÃO IMPLEMENTADO\n" \
        "Informe qualquer outra coisa para sair "

    print(welcome_message)
        
    option = input("Informe a opção: ")
    print("\n")
    if(option == "1"):
        FileToDatabase.read_file_and_load_sqlite3()
    elif(option == "2"):
        FileToFile.read_csv_and_load_fwf()
    elif(option == "3"):
        FileToFile.read_fwf_and_load_csv()
    elif(option == "4"):
        FileToDatabase.read_file_and_load_sqlserver()
        print("> AVISO: Funcionalidade não implementada ")
    elif(option == "5"):
        FileToDatabase.read_file_and_load_oracle()
        print("> AVISO: Funcionalidade não implementada ")
    elif(option == "6"):
        FileToDatabase.read_file_and_load_mysql()
        print("> AVISO: Funcionalidade não implementada ")
    
    input("> Aperte Enter para continuar...")