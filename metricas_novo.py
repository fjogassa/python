import pandas as pd
import datetime as dt

class LoadMetricas:
  arquivo_inicial = pd.DataFrame()
  def __init__(self):
    self.arquivo_inicial = pd.read_csv(".\\arquivos\\metricas.csv")

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
  metricas.arquivo_inicial.to_csv("novo_metricas.csv", sep=";", decimal=".")