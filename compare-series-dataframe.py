import pandas as pd


def create_series(value):
    serie = pd.Series(value)
    return serie


def create_dataframe(value):
    df = pd.DataFrame(value)
    return df


if __name__ == "__main__":
    dict_to_pd = {
        "names": ["john doe", "jane doe", "Eureka"],
        "meal": ["carne", "arroz", "feijão"],
        "after": ["brigadeiro", "arroz doce", "pudim"],
    }

    serie = create_series(dict_to_pd)
    df = create_dataframe(dict_to_pd)

    print(f"{serie} \n {df}")
