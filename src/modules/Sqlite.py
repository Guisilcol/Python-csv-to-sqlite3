import pandas as pd
import sqlite3 

def access_database(database_filepath: str) -> sqlite3.Connection:
    return sqlite3.connect(database_filepath) 

def load_csv(dataframe: pd.DataFrame, table_name: str, connection: sqlite3.Connection) -> None:
    dataframe.to_sql(name=table_name, con=connection, if_exists="replace", index=False)
    