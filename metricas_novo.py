import pandas as pd
import datetime as dt

class LoadMetricas:
  arquivo_inicial = pd.DataFrame()
  def __init__(self):
    self.arquivo_inicial = pd.read_csv(".\\arquivos\\metricas.csv")

  def criaDataFrameSaida(self, file: pd.DataFrame, campos) -> pd.DataFrame:
    return self.arquivo_inicial[campos].copy()

  def limpaCamposDataNula(self, campo:str):    
      self.arquivo_inicial[campo].fillna(value=pd.NaT, inplace=True)      

  def diferencaEntreDatas(self, coluna1:str, coluna2:str, colunaResultado: str) -> pd.DataFrame:    
    for index in range(len(self.arquivo_inicial)):
      self.arquivo_inicial.loc[index, colunaResultado] = int(0)
      if (not pd.isnull(self.arquivo_inicial[coluna1][index])) and (not pd.isnull(self.arquivo_inicial[coluna2][index])):
        if (self.arquivo_inicial[coluna2][index] >= self.arquivo_inicial[coluna1][index]):          
          self.arquivo_inicial.loc[index, colunaResultado] = (self.arquivo_inicial[coluna2][index] - self.arquivo_inicial[coluna1][index]).days
        else:          
          self.arquivo_inicial.loc[index, colunaResultado]= (self.arquivo_inicial[coluna1][index] - self.arquivo_inicial[coluna2][index]).days          

if __name__ == "__main__":
  metricas = LoadMetricas()  
  metricas.arquivo_inicial["Code review"] = pd.to_datetime(metricas.arquivo_inicial["Code review"])    
  metricas.arquivo_inicial["In Progress"] = pd.to_datetime(metricas.arquivo_inicial["In Progress"])      
  metricas.limpaCamposDataNula("Code review")
  metricas.limpaCamposDataNula("In Progress")
  metricas.diferencaEntreDatas("Code review", "In Progress", "Devtime")    
  campos_to_copy = ['id', 'To Do', 'In Progress', 'Assignee']
  df = metricas.criaDataFrameSaida(metricas.arquivo_inicial, campos_to_copy)
  print(df)
  metricas.arquivo_inicial.to_csv("novo_metricas.csv", sep=";", decimal=".")  