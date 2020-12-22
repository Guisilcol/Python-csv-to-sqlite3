import re 
import io
import pandas as pd 

def delimited_file_to_dataframe(filepath):
    colunm_separator = None
    parameters = None
    
    try:
        parameters = get_parameters_of_file(filepath)
        colunm_separator = parameters["sep"] if parameters["sep"] != None else ";"
        
    except Exception:
        colunm_separator = ";"
        
    finally:
        with open(filepath) as file:
            data = get_file_without_parameters(filepath)
            return pd.read_csv(data, sep=colunm_separator)     
 
""" Será implementada posteriormente 
def fixed_width_file_to_dataframe(filepath):
    parameters = None 
    
    try:
        parameters = get_parameters_of_file(filepath)
        
    except Exception:
        yield IOError(message="> Erro: Não foi possível restaurar os parâmetros do arquivo")
"""

def get_parameters_of_file(filepath) -> dict:
    data = None
    
    with open(filepath) as file:
        file = open(filepath)
        data = file.read()
         
    begin_parameter_index = data.index("/*") + 2
    end_parameter_index = data.index("*/", begin_parameter_index)
    
    result = re.search("\/\*([^\)]+)\*\/", data).group()
    
    raw_parameters = result[3 : result.__len__() - 2]

    parameters = {}
    
    for line in raw_parameters.splitlines():
        (key, val) = line.split("=")
        parameters[key] = val
    
    return parameters

def get_file_without_parameters(filepath: str) -> io.StringIO:
    with open(filepath) as file:
        data_raw = file.read()
        data_raw_without_parameters = re.sub("\/\*([^\)]+)\*\/", "", data_raw)
        data = io.StringIO(data_raw_without_parameters)
        return data