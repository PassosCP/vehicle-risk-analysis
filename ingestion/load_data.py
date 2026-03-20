print("🔥 SCRIPT INICIADO")
import pandas as pd
import sqlite3
import os

def load_data():
    print("🔄 Carregando dados de roubo de veículos...")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_path = os.path.join(BASE_DIR, 'data', 'roubo_veiculos_rj.csv')
    db_dir = os.path.join(BASE_DIR, 'database')
    db_path = os.path.join(db_dir, 'veiculos.db')

    os.makedirs(db_dir, exist_ok=True)

    df = pd.read_csv(csv_path)

    print(df.head())

    conn = sqlite3.connect(db_path)
    df.to_sql('roubos', conn, if_exists='replace', index=False)
    conn.close()

    print("✅ Dados carregados no banco!")

    return df

if __name__ == "__main__":
    load_data()