# 1 Quantas linhas e colunas possui o nosso conjunto de dados?
# 2 Há valores nulos no DataFrame?
# 3 Qual o número médio de pessoas em situação de rua por região do Brasil em nosso DataFrame?
# 4 Qual região tem proporcionalmente a maior quantidade de pessoas nessa situação? E qual tem menos?
import pandas as pd


def create_df(value):
    return pd.DataFrame(value)


def quest_1(df):
    print(df.shape)


def quest_2(df):
    print(df.info())


def quest_3(df):
    print(df.describe())


def quest_4(df):
    print(df.describe())


if __name__ == "__main__":
    values_to_dataframe = {
        "Grande Região": ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
        "Número de Municípios": [450, 1794, 1668, 1191, 467],
        "População em situação de rua": [4399, 22864, 49792, 16021, 8777],
        "Total de Municípios (%)": [8.10, 32.20, 29.90, 21.40, 8.40],
        "Total em situação de rua (%)": [4.32, 22.45, 48.89, 15.73, 8.62],
    }

    df = create_df(values_to_dataframe)
    # quest_1(df)
    # quest_2(df)
    # quest_3(df)
    # quest_4(df)
