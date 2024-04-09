import pandas as pd


def create_series(value):
    serie = pd.Series(value)
    return serie


def create_dataframe(value):
    df = pd.DataFrame(value)
    return df


if __name__ == "__main__":
    dict_to_pd = {
        "names": ["john doe", "jane doe", "Eureka", "nome1", "nome2", "nome3"],
        "meal": ["carne", "arroz", "feijão", "comida1", "comida2", "comida3"],
        "after": [
            "brigadeiro",
            "arroz doce",
            "pudim",
            "sobrimesa1",
            "sobrimesa2",
            "sobrimesa3",
        ],
    }

    serie = create_series(dict_to_pd)
    df = create_dataframe(dict_to_pd)

    print(f"{serie} \n {df} \n")
    print(f"{serie.shape} \n {df.shape} \n")
    print(f"{serie} \n {df.columns} \n")  # columns works only in df
    print(f"{serie.describe()} \n {df.describe()} \n")
    print(f"{serie.info()} \n \n")
    print(f"\n {df.head()} \n")
    print(f"\n {df.tail()} \n")
