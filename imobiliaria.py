import arquivos_csv as csv

arquivo = csv.Arquivo(".\\arquivos\\aluguel.csv", ";", ".")
file = arquivo.le_arquivo()
print(file['Tipo'])