import arquivos_csv as csv
import pandas as pd

# Lendo arquivo
#arquivo_csv = csv.Arquivo(".\\arquivos\metricas.csv", ",", ".")
arquivo_csv = pd.read_csv(".\\arquivos\metricas.csv", sep=",", decimal=".", skipfooter=1, date_parser=lambda x: pd.to_datetime(x, format='%d.%m.%Y'))
print(arquivo_csv['Backlog'])
#arquivo_metricas = arquivo_csv.le_arquivo()

# Pegando somente as colunas que interessam
#arquivo = arquivo_csv.getColunas(arquivo_metricas, ['id', 'Backlog'])
#print(arquivo['Backlog'].astype('datetime64[as]'))