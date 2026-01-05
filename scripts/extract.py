# Passo 1: importar bibliotecas
import requests
from bs4 import BeautifulSoup
import os

# Passo 2: função para exibir nossos dados 
def extract_data(output_dir):

    # definir as variaveis que vão receber parametros das bibliotecas que importamos
    url = "https://en.wikipedia.org/wiki/COVID-19_pandemic"

    headers = {
        "User-Agent": "WebScrapingETL/1.0 (educational project)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # definir uma variavel para econtrar todas as tabelas e retornar quantas tabelas tem na pagina do site
    tables = soup.find_all("table", {"class":"wikitable"})
    print(f"Numeros de tabelas encontradas : {len(tables)}")

    # salvar cada variavel para análise
    for i, table in enumerate(tables):
        file_path = os.path.join(output_dir, f"table_{i}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(table))
        print(f"Tabela {i} salvo em: {file_path}")

# função para retornar nossa aplicação e executar a nossa função
if __name__ == "__main__":
    raw_data_dir = os.path.join("data","raw")
    os.makedirs(raw_data_dir, exist_ok=True)
    extract_data(raw_data_dir)