import arquivos_csv as arquivocsv
import pandas as pd
import datetime as dt

class LoadMetricas:  
  campos_saida = ["id","Backlog","To Do","In Progress","Code review","In Code Review","Waiting Deploy","To Test"
                  ,"Testing","To Release","Done","Type","Priority","Components","Assignee","Blocked Days","Link Epic","Size"]

  def __init__(self, nomeArquivo, separador, decimalSeparador):
    self._arquivo = arquivocsv.ArquivoCSV(nomeArquivo, separador, decimalSeparador)
    self.arquivo_inicial = self._arquivo.leArquivo()

  # Método que calcula a diferença em dias de duas datas (coluna1 e coluna2) e atribui-se na colunaResultado
  def diferencaEntreDatas(self, coluna1:str, coluna2:str, colunaResultado: str) -> pd.DataFrame:        
    for index in range(len(self.arquivo_inicial)):
      self.arquivo_inicial.loc[index, colunaResultado] = int(0)
      if (not pd.isnull(self.arquivo_inicial[coluna1][index])) and (not pd.isnull(self.arquivo_inicial[coluna2][index])):
        if (self.arquivo_inicial[coluna2][index] >= self.arquivo_inicial[coluna1][index]):          
          self.arquivo_inicial.loc[index, colunaResultado] = (self.arquivo_inicial[coluna2][index] - self.arquivo_inicial[coluna1][index]).days
        else:          
          self.arquivo_inicial.loc[index, colunaResultado]= (self.arquivo_inicial[coluna1][index] - self.arquivo_inicial[coluna2][index]).days          

if __name__ == "__main__":  
  metricas = LoadMetricas(".\\arquivos\\metricas.csv", ",", ".")

  if (not metricas.arquivo_inicial.empty):
    metricas.arquivo_inicial["Code review"] = pd.to_datetime(metricas.arquivo_inicial["Code review"])    
    metricas.arquivo_inicial["In Progress"] = pd.to_datetime(metricas.arquivo_inicial["In Progress"])      
    metricas.arquivo_inicial["Done"] = pd.to_datetime(metricas.arquivo_inicial["Done"])      

    metricas._arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "Code review")
    metricas._arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "In Progress")
    metricas._arquivo.limpaCamposDataNula(metricas.arquivo_inicial, "Done")
    
    metricas.diferencaEntreDatas("Code review", "In Progress", "Devtime")    
    campos_to_copy = ['id', 'To Do', 'In Progress', 'Assignee']    
    
    metricas._arquivo.criaArquivo(metricas._arquivo.criaDataFrameSaida(metricas.arquivo_inicial, campos_to_copy), "novo_metricas",";",".")    