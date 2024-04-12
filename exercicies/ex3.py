import pandas as pd


# 1 Gostaria de ter uma visão geral sobre as
# informações contidas na base de dados fifa_audience.

# 2 Com a finalidade de ter a visibilidade dos países com
# maior participação no compartilhamento global de transmissões,
# mostre na tela apenas os países com porcentagem de compartilhamento
# global (population_share) maior que 2.

# 3 a quantidade de países em cada confederação.

# 4 mostre na tela quais são os países que participaram da
# conferencia CONMEBOL.

# 5 Mostre a média de audiência dos países que fazem parte
# da confederação UEFA e limite em duas casas decimais.


class fifa_audience:
    def __init__(self):
        self.df = pd.read_csv("./fifa_audience.csv")

    def info_fifa_audience(self):
        return self.df.info()

    def population_share(self, number):
        df = self.df
        return df.loc[df["population_share"] > number]

    def country_in_conf(self):
        df = self.df
        grouped_country = df.groupby("confederation")["country"]
        return grouped_country.count().reset_index(name="count")

    def country_by_conf(self, name):
        df = self.df
        return df["country"].loc[df["confederation"] == name]

    def audience_by_conf(self, name):
        df = self.df
        audience = df.loc[df["confederation"] == name]
        return audience["tv_audience_share"].mean()


if __name__ == "__main__":
    new_f_a = fifa_audience()
    # new_f_a.info_fifa_audience()
    # print(new_f_a.population_share(2))
    # print(new_f_a.country_in_conf())
    # print(new_f_a.country_by_conf("CONMEBOL"))
    print(new_f_a.audience_by_conf("UEFA"))
