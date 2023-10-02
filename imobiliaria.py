import arquivos_csv as csv
import pandas as pd

#arquivo = pd.read_csv("aluguel.csv", sep=";", decimal=".")


arquivo = csv.Arquivo()

arquivo.nome_arquivo = "aluguel.csv"
arquivo.separador = ";"
arquivo.decimal_separator = "."

arquivo.manipula_arquivo()

print(arquivo)