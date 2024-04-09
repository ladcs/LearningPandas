import pandas as pd


def create_series(values):

    serie = pd.Series(values)
    print(serie)


if __name__ == "__main__":
    cavaleiro_de_bronze = ["Ikki", "Hyoga", "Seyia", "Shiryu", "Shun"]
    create_series(cavaleiro_de_bronze)
    sailors = {
        "Moon": "Usagi",
        "Mercury": "Ami",
        "Mars": "Rei",
        "Jupter": "Makoto",
        "Venus": "Minako",
    }

    print("\n\n\n\n")
    create_series(sailors)
