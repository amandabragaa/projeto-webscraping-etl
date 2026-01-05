# Passo 1: importar bibliotecas
import pandas as pd
from bs4 import BeautifulSoup
import os
from io import StringIO

# Passo 2: acessar e tratar as tabelas
def transform_table_0(input_path, output_path):
    """Essa função transformara a tabela do IFR(fatalidade por faixa etaria)"""
    with open(input_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file,"html.parser")
    table = soup.find("table")
    df = pd.read_html(StringIO(str(table)))[0]

    # acessar as colunas da tabela e converter para csv
    df.columns = ["Age group", "IFR"]
    df.to_csv(output_path, index=False)
    print(f"Tabela IFR transformada e salva em {output_path}")


def transform_table_1(input_path, output_path):
    """tansforma a tabela variantsof concerne"""
    with open(input_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    table = soup.find("table")
    df = pd.read_html(StringIO(str(table)))[0]

    df.columns = ["Name", "Lineage", "Detected", "Countries", "Priority"]
    df.to_csv(output_path, index=False)
    print(f"Tabela Variants of concerne transformada e salva em: {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #caminho para o dir pai
    raw_data_dir = os.path.join(base_dir, "data", "raw")
    processed_data_dir = os.path.join(base_dir, "data", "processed")
    os.makedirs(processed_data_dir, exist_ok=True)

    # chamar as função 0
    transform_table_0(
        input_path=os.path.join(raw_data_dir, "table_0.html"),
        output_path=os.path.join(processed_data_dir, "ifrs.csv"),
    )

    # chamar as função 01
    transform_table_1(
        input_path=os.path.join(raw_data_dir, "table_1.html"),
        output_path=os.path.join(processed_data_dir, "variants.csv"),
    )