import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.db_config import DB_CONFIG
import pandas as pd
import psycopg2

# carregar o ifrs.csv
def load_ifrs(csv_path):
    # estabeleccer conexão com o postgre
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # crir a tabela que vi receber os ados do ifrs
    create_table_query = """
            CREATE TABLE IF NOT EXISTS ifrs
            (
                age_group TEXT,
                ifr TEXT
            );
"""

    #executar para criar a tabela ifr
    cursor.execute(create_table_query)
    conn.commit()

    # inserir dados
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO ifrs (age_group, ifr) VALUES (%s,%s)", tuple(row))
    # fechar conexão
    conn.commit()
    cursor.close
    conn.close()
    print("Dados IFRs carregados no banco de dados!")

def load_variants(csv_path):
    # estabeleccer conexão com o postgre
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # criar tabelasvarians
    create_table_query = """
    CREATE TABLE IF NOT EXISTS variants(
        name TEXT,
        lineage TEXT,
        detected TEXT,
        countries INT,
        priority TEXT
    )
    """
    #executar para criar a tabela ifr
    cursor.execute(create_table_query)
    conn.commit()

    # inserir dados
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO variants (name, lineage, detected, countries, priority) VALUES (%s, %s, %s, %s, %s)",
            tuple(row)
        )
    # fechar conexão
    conn.commit()
    cursor.close
    conn.close()
    print("Dados IFRs carregados no banco de dados!")    

# chamando a função final para executar as funções
if __name__ == "__main__":
    processed_data_dir = os.path.join("data", "processed")
    load_ifrs(csv_path=os.path.join(processed_data_dir, "ifrs.csv"))
    load_variants(csv_path=os.path.join(processed_data_dir, "variants.csv"))


