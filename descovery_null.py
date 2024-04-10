import pandas as pd


df = pd.read_csv("chuvas_morumbi.csv")

df.info()  # one column with Non-Null Count

# print(df.isnull())
# print(df.isna())

# print(df.isna().sum())
print(df.isnull().sum())
