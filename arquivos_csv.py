import pandas as pd

class Arquivo:
  nome_arquivo:str = None
  csv_separator:str = None
  decimal_separator:str = None
  arquivo_data_frame = None
  # constructor
  def __init__(self, nome_arquivo = None, csv_separator = None, decimal_separator = None):
    self.nome_arquivo = nome_arquivo
    self.csv_separator = csv_separator
    self.decimal_separator = decimal_separator

  def le_arquivo(self) -> pd.DataFrame:
    return pd.read_csv(self.nome_arquivo, sep=self.csv_separator, decimal=self.decimal_separator)
  
  def getColunas(self, file, colunas):
    return file[colunas]

  def manipula_arquivo(self, file):        
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
  def cria_arquivo(self, nome_arquivo_destino:str = None) -> None:    
    aprovados = self.arquivo_data_frame['Aprovado'] == True
    df_aprovados = self.arquivo_data_frame[aprovados]
    print(f'Lista dos Aprovados\n {df_aprovados}') 
    
    df_aprovados.to_csv(nome_arquivo_destino, sep=';')
    df_aprovados.replace({'Notas':7.0}, 8.0, inplace=True)
    print(f'Aprovados: {df_aprovados}')

if __name__ == "__main__":
  arquivo_csv = Arquivo('.\\arquivos\\alunos.csv', ',', '.')
  arquivo_data_frame = arquivo_csv.le_arquivo()
  print(arquivo_data_frame)
  arquivo_data_frame = arquivo_csv.manipula_arquivo(arquivo_data_frame)
  print(f'Após a manipulação\n {arquivo_data_frame}')
  #arquivo_csv.cria_arquivo('alunos_aprovados.csv')