import arquivos_csv as arquivocsv
import pandas as pd
import datetime as dt

class LoadMetricas:
  arquivo_inicial = pd.DataFrame()
  _arquivo = None

  def __init__(self):
    self.arquivo_inicial = _arquivo.leArquivo()

  def diferencaEntreDatas(self, coluna1:str, coluna2:str, colunaResultado: str) -> pd.DataFrame:    
    for index in range(len(self.arquivo_inicial)):
      self.arquivo_inicial.loc[index, colunaResultado] = int(0)
      if (not pd.isnull(self.arquivo_inicial[coluna1][index])) and (not pd.isnull(self.arquivo_inicial[coluna2][index])):
        if (self.arquivo_inicial[coluna2][index] >= self.arquivo_inicial[coluna1][index]):          
          self.arquivo_inicial.loc[index, colunaResultado] = (self.arquivo_inicial[coluna2][index] - self.arquivo_inicial[coluna1][index]).days
        else:          
          self.arquivo_inicial.loc[index, colunaResultado]= (self.arquivo_inicial[coluna1][index] - self.arquivo_inicial[coluna2][index]).days          

if __name__ == "__main__":  
  _arquivo = arquivocsv.ArquivoCSV(".\\arquivos\\metricas.csv", ",", ".")  
  metricas = LoadMetricas()

  if (not metricas.arquivo_inicial.empty):
    metricas.arquivo_inicial["Code review"] = pd.to_datetime(metricas.arquivo_inicial["Code review"])    
    metricas.arquivo_inicial["In Progress"] = pd.to_datetime(metricas.arquivo_inicial["In Progress"])      
    metricas.arquivo_inicial["Done"] = pd.to_datetime(metricas.arquivo_inicial["Done"])      

    _arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "Code review")
    _arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "In Progress")
    _arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "Done")
    
    metricas.diferencaEntreDatas("Code review", "In Progress", "Devtime")    
    campos_to_copy = ['id', 'To Do', 'In Progress', 'Assignee']
    df = _arquivo.criaDataFrameSaida(metricas.arquivo_inicial, campos_to_copy)    
    _arquivo.criaArquivo(df, "novo_metricas",";",".")    