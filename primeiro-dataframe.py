import pandas as pd


def situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"


def dataframe_notas():
    dict_notas = {
        "nome": ["Maria", "João", "Fernanda", "Túlio"],
        "primeira-nota": [9, 8, 7, 8],
        "segunda-nota": [8, 7, 9, 3],
    }

    df = pd.DataFrame(dict_notas)

    df["media"] = (df["primeira-nota"] + df["segunda-nota"]) / 2
    df["situação"] = df["media"].apply(situacao)

    print(df)


dataframe_notas()
