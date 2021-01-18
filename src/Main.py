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
        "1 - Exportar dados de arquivos para banco de dados SQLITE3 \n" \
        "2 - Transformar arquivos .csv em arquivos posicionais \n" \
        "3 - Transformar arquivos posicionais em arquivos .csv \n" \
        "4 - Exportar os arquivos em tabelas SQLSERVER - NÃO IMPLEMENTADO\n" \
        "5 - Exportar os arquivos em tabelas ORACLE - NÃO IMPLEMENTADO\n" \
        "6 - Exportar os arquivos em tabelas MYSQL - NÃO IMPLEMENTADO\n" \
        "Informe qualquer outra coisa para sair "

    print(welcome_message)
        
    option = input("Informe a opção: ")
    
    if(option == "1"):
        FileToDatabase.read_file_and_load_sqlite3()
    elif(option == "2"):
        FileToFile.read_csv_and_load_fwf()
    elif(option == "3"):
        FileToFile.read_fwf_and_load_csv()
    elif(option == "4"):
        FileToDatabase.read_file_and_load_sqlserver()
    elif(option == "5"):
        FileToDatabase.read_file_and_load_oracle()
    elif(option == "6"):
        FileToDatabase.read_file_and_load_mysql()
    else:
        print("> Erro: A opção informada é inválida.")
    
    input("> Aperte Enter para continuar...")

    
    