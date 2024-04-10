import pandas as pd


df = pd.read_csv("./chuvas_morumbi.csv")

print(df.iloc[0:5])
print(df.iloc[5])
