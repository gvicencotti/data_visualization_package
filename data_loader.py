import pandas as pd
import sqlite3

def load_csv(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        return dataframe
    except Exception as e:
        print(f"Erro ao carregar CSV": {e})
        return None
    
def load_json(file_path):
    try:
        dataframe = pd.read_json(file_path)
        return dataframe
    except Exception as e:
        print(f"Erro ao carregar JSON": {e})
        return None
    
def load_sql(database_path, query):
    try:
        conn = sqlite3.connect(database_path)
        dataframe = pd.read_sql_query(query, conn)
        conn.close()
        return dataframe
    except Exception as e:
        print(f"Erro ao carregar dados SQL": {e})
        return None