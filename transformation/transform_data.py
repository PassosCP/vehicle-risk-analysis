import pandas as pd

def transform_data(df):

    print("🔄 Iniciando transformação dos dados...")

    # 🔹 Agregação
    df_municipio = df.groupby('municipio')['roubos'].sum().reset_index()

    print("\n📊 Total de roubos por município:")
    print(df_municipio)

    # 🔹 Média
    media_geral = df_municipio['roubos'].mean()

    # 🔹 Flag
    df_municipio['risco_alto'] = df_municipio['roubos'] > media_geral

    # =====================================================
    # 🔹 RANKING (TEM QUE ESTAR DENTRO)
    # =====================================================
    df_municipio = df_municipio.sort_values(by='roubos', ascending=False)

    print("\n🏆 Ranking:")
    print(df_municipio)

    # =====================================================
    # 🔹 PARTICIPAÇÃO
    # =====================================================
    total = df_municipio['roubos'].sum()

    df_municipio['percentual'] = (df_municipio['roubos'] / total) * 100

    # =====================================================
    # 🔹 CLASSIFICAÇÃO
    # =====================================================
    def classificar_risco(valor, media):
        if valor > media * 1.5:
            return "ALTO"
        elif valor > media:
            return "MÉDIO"
        else:
            return "BAIXO"

    df_municipio['nivel_risco'] = df_municipio['roubos'].apply(
        lambda x: classificar_risco(x, media_geral)
    )

    print("\n🚨 Classificação final:")
    print(df_municipio)

    print("\n✅ Transformação concluída!")

    return df_municipio

df_municipio.to_csv('data/resultado_final.csv', index=False)