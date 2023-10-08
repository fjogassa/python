import pandas as pd
from datetime import datetime

class ArquivoCSV:
  nome_arquivo:str = None
  csv_separator:str = None
  decimal_separator:str = None
  arquivo_data_frame = None

  # constructor
  def __init__(self, nome_arquivo = None, csv_separator = None, decimal_separator = None):
    self.nome_arquivo = nome_arquivo
    self.csv_separator = csv_separator
    self.decimal_separator = decimal_separator

  def leArquivo(self) -> pd.DataFrame:
    try:
      return pd.read_csv(self.nome_arquivo, sep=self.csv_separator, decimal=self.decimal_separator)
    except Exception as e:
      print(f'Operação foi finalizada por um erro: {e}')
      return None
          
  def criaDataFrameSaida(self, file: pd.DataFrame, campos) -> pd.DataFrame:
    return file[campos].copy()
  
  def getColunas(self, file, colunas):
    return file[colunas]

  def manipulaArquivo(self, file):        
    # Filtra os dez primeiros resultados
    file.head(10)
    file.isnull().sum()
    
    # Tratamento para converter notas nulas em zero
    notas_nulas = {"Notas": 0,"Media": 0}
    file.fillna(value = notas_nulas, inplace = True)

    # Removendo com base no filtro Nome = Alice ou Nome = Carlos
    alunos_que_sairam = file.query('Nome == "Alice" | Nome == "Carlos"').index
    file.drop(alunos_que_sairam, axis=0, inplace=True)
    #print(f'Sem os alunos que saíram\n {file}') 
    return file

  # Criando arquivo CSV
  def criaArquivo(self, file:pd.DataFrame, nome_arquivo_destino, separador, decimalSeparador: str) -> None:
    if str(nome_arquivo_destino).lstrip() != "":
      file.to_csv(nome_arquivo_destino + datetime.now().strftime("%H%M%S%f") + ".csv", sep=separador, decimal=decimalSeparador)
    else:
      raise Exception("Não foi possível criar o arquivo")

  # Limpa os campos do tipo datetime para NaT (nulo)  
  def limpaCamposDataNula(self, file: pd.DataFrame, campo) -> None:
    file[campo].fillna(value=pd.NaT, inplace=True)

if __name__ == "__main__":
  arquivo_csv = ArquivoCSV('.\\arquivos\\alunos.csv', ',', '.')
  arquivo_data_frame = arquivo_csv.leArquivo()
  print(arquivo_data_frame)
  arquivo_data_frame = arquivo_csv.manipulaArquivo(arquivo_data_frame)
  print(f'Após a manipulação\n {arquivo_data_frame}')  