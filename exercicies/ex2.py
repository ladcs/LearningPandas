# 1 Qual o dia da semana em que o queijo muçarela está com o menor preço?
# 2 Qual o nome do fornecedor onde o tomate esteve com o maior preço histórico?
# 3 Em qual/quais dia/dias da semana o fornecedor soma pão aparentemente não
# abriu as portas?
# 4 Crie um novo DataFrame com o preço médio de cada produto pesquisado.

import pandas as pd


def quest_1(df):
    cheese = df.loc[df["produto"] == "queijo muçarela"]
    low_price = df["preco_reais"].loc[df["produto"] == "queijo muçarela"].min()
    print(cheese["dia_da_semana"].loc[cheese["preco_reais"] == low_price])


def quest_2(df):
    price = df["preco_reais"].loc[df["produto"] == "tomate"].max()
    tomate = df.loc[df["produto"] == "tomate"]

    print(tomate["nome_do_fornecedor"].loc[tomate["preco_reais"] == price])


def quest_3(df):
    print(
        df["dia_da_semana"].loc[
            df["preco_reais"].isnull() & (df["nome_do_fornecedor"] == "soma pão")
        ]
    )


def quest_4(df):
    other_df = (
        df.groupby(by="produto")
        .mean(numeric_only=True)
        .rename(columns={"preco_reais": "preco_medio"})
    )
    print(other_df)


if __name__ == "__main__":
    df = pd.read_csv("pesquisa_pao_na_chapa.csv")
    # quest_1(df)
    # quest_2(df)
    # quest_3(df)
    quest_4(df)
