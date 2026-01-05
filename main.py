import os
from scripts.extract import extract_data
from scripts.transform import transform_table_0, transform_table_1
from scripts.load import load_ifrs, load_variants

def main():
    # Diretórios de entrada e saída
    raw_data_dir = os.path.join("data", "raw")
    processed_data_dir = os.path.join("data", "processed")

    # Criar diretórios caso não existam
    os.makedirs(raw_data_dir, exist_ok=True)
    os.makedirs(processed_data_dir, exist_ok=True)

    # Etapa 1: Extração
    print("Iniciando Extração...")
    extract_data(raw_data_dir)
    print("Extração concluída.\n")

    # Etapa 2: Transformação
    print("Iniciando Transformação...")
    transform_table_0(
        input_path=os.path.join(raw_data_dir, "table_0.html"),
        output_path=os.path.join(processed_data_dir, "ifrs.csv"),
    )
    transform_table_1(
        input_path=os.path.join(raw_data_dir, "table_1.html"),
        output_path=os.path.join(processed_data_dir, "variants.csv"),
    )
    print("Transformação concluída.\n")

    # Etapa 3: Carga
    print("Iniciando Carga...")
    load_ifrs(csv_path=os.path.join(processed_data_dir, "ifrs.csv"))
    load_variants(csv_path=os.path.join(processed_data_dir, "variants.csv"))
    print("Carga concluída.\n")

    print("Pipeline ETL concluído com sucesso!")

if __name__ == "__main__":
    main()