import arquivos_csv as csv

arquivo = csv.Arquivo("aluguel.csv", ";", ".")
file = arquivo.le_arquivo()
print(file['Tipo'])