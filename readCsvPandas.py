import pandas as pd


def readCsv(path):
    return pd.read_csv(path)


def readJson(path):
    return pd.read_json(path)


if __name__ == "__main__":
    path = "../chuvas_morumbi.csv"
    dfCsv = readCsv(path)

    dfCsv.to_json("./chuvas_morumbi.json")

    path = "./chuvas_morumbi.json"

    dfJson = readJson(path)
    # print(dfJson)
    print(dfJson.loc[dfJson["intervalo"] == "2022-07-31 00:00:00 UTC"])
    # print(dfJson.loc[[20]])
