import pandas as pd


def situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"


def dataframe_notas():
    dict_notas = {
        "nome": ["Maria", "João", "Fernanda", "Túlio"],
        "primeira-nota": [9, 8, 7, 8],
        "segunda-nota": [8, 7, 9, 3],
    }

    data_frame = pd.DataFrame(dict_notas)

    data_frame["media"] = (data_frame["primeira-nota"] + data_frame["segunda-nota"]) / 2
    data_frame["situação"] = data_frame["media"].apply(situacao)

    print(data_frame)


dataframe_notas()
