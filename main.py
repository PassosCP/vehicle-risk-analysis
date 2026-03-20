from ingestion.load_data import load_data
from transformation.transform_data import transform_data

df = load_data()

if df is None:
    print("Erro na carga")
    exit()

df = transform_data(df)

print("✅ Pipeline executado com sucesso!")