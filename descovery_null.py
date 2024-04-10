import pandas as pd


df = pd.read_csv("chuvas_morumbi.csv")

df.info()  # one column with Non-Null Count

# print(df.isnull())
# print(df.isna())

# print(df.isna().sum())
print(df.isnull().sum())

# isnull e isna fazem a mesma coisa, retorna uma tabela com true ou false,
# onde true é nulo.
# com o uso do sum retorno a quantidade de valores nulos.
