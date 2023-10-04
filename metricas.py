import pandas as pd

from datetime import datetime

class Metricas:  
  colunas_data = ['Backlog','To Do','In Progress','Code review','In Code Review','Waiting Deploy',
                  'To Test','Testing','To Release','Done','Data para entrega','Previsto para']
  colunas_metricas = ['id','Backlog','To Do','In Progress','Code review','In Code Review','Waiting Deploy',
                      'To Test','Testing','To Release','Done','Type','Assignee','Project','Blocked Days','Link Epic','Size']
  colunas_calculadas: dict = {'Dev Time': ('Code review', 'In Progress'),
                        'Dev To Code Review': ('Waiting Deploy',  'In Progress'),
                        'Cycle Time': ('Done', 'In Progress'),
                        'Lead Time': ('Done', 'To Do'),
                        'Progress to Deploy': ('Waiting Deploy', 'In Progress')}
  
  arquivo_csv: pd.DataFrame = None
  arquivo_saida: pd.DataFrame = None

  def __init__(self) -> None:    
    # Lendo arquivo
    self.arquivo_csv = pd.read_csv(".\\arquivos\metricas.csv", sep=",", decimal=".")    
    #print(f'Antes: {self.arquivo_csv}')
    #self.arquivo_csv.fillna(None, inplace=True)
    #print(f'Depois: {self.arquivo_csv}')

  # Mudando o tipo da coluna de object para Datetime pelo nome das colunas
  def trataColunaData(self) -> None:
    # Converter as colunas de data para o tipo date time
    for i in self.colunas_data:      
      self.arquivo_csv[i] = pd.to_datetime(self.arquivo_csv[i])    
    print(f'Antes: {self.arquivo_csv.query("Done.notnull()")["Done"].head(10)}')    
    registros_nulo = self.arquivo_csv.query('Done.isnull()').index
    self.arquivo_csv.drop(registros_nulo, axis=0, inplace=True)    
    print(f'Depois: {self.arquivo_csv["Done"].head(10)}')
    #self.arquivo_csv['Done'].fillna(value=None, inplace=True)
    #print(f'Depois: {self.arquivo_csv["Done"].isnull().sum()}')

    # Alimentar os campos calculados
    for key, value in self.colunas_calculadas.items():                  
      self.arquivo_csv[key] = self.getDiferencaDataEmDias(datetime(self.arquivo_csv[value[0]]), datetime(self.arquivo_csv[value[0]]))

  def getDiferencaDataEmDias(self, data1, data2):    
    return (data1 - data2).days
  
  def salvaArquivo(self, nome_arquivo_destino: str = "") -> None:
    if (nome_arquivo_destino != ""):
      self.arquivo_saida.to_csv(nome_arquivo_destino + datetime.now().strftime("%H%M%S%f") + ".csv", sep=";", mode="x")

  # Gerar arquivo de destino com base nos dados da origem
  def geraArquivoDestino(self) -> pd.DataFrame:
    return self.arquivo_csv[self.colunas_metricas]

if __name__ == '__main__':
  try:      
    metricas = Metricas()    
    arquivo_saida = metricas.geraArquivoDestino()
    metricas.trataColunaData()
    #metricas.__salvaArquivo("arquivo_metricas")
  except FileExistsError:
    print("Arquivo já existe")
  except Exception as e:
    print(f'Ocorreu um erro: {e}')  
