import pandas as pd


primeira_nota = pd.DataFrame(
    {
        "nome": ["maria", "joão", "pedro", "ana"],
        "primeira_nota": [9, 8, 7, 8],
    }
)

segunda_nota = pd.DataFrame(
    {
        "nome": ["maria", "joão", "pedro", "ana", "Josefa"],
        "segunda_nota": [8, 7, 9, 3, 6],
    }
)

par_de_notas = primeira_nota.merge(segunda_nota, how="right")  # right se usa
# para o que estiver dentro do merge left a primeira df
print(par_de_notas)
