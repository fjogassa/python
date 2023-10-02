import pandas as pd

class Arquivo:
  nome_arquivo:str = None
  separador:str = None
  decimal_separator:str = None
  arquivo_data_frame: any = None
  # constructor
  def __init__(self, nome_arquivo = None, separador = None, decimal_separator = None) -> None:
    self.nome_arquivo = nome_arquivo
    self.separador = separador
    self.decimal_separator = decimal_separator

  def manipula_arquivo(self):
    self.arquivo_data_frame = pd.read_csv(self.nome_arquivo, sep = self.separador, decimal = self.decimal_separator)    
    print(self.arquivo_data_frame)
    # Filtra os dez primeiros resultados
    self.arquivo_data_frame.head(10)
    self.arquivo_data_frame.isnull().sum()
    
    # Tratamento para converter notas nulas em zero
    notas_nulas = {"Notas": 0,"Media": 0}
    self.arquivo_data_frame.fillna(value = notas_nulas, inplace = True)

    # Removendo com base no filtro Nome = Alice ou Nome = Carlos
    alunos_que_sairam = self.arquivo_data_frame.query('Nome == "Alice" | Nome == "Carlos"').index
    self.arquivo_data_frame.drop(alunos_que_sairam, axis=0, inplace=True)
    print(f'Sem os alunos que saíram\n {self.arquivo_data_frame}')    

  # Criando arquivo CSV
  def cria_arquivo(self, nome_arquivo_destino:str = None) -> None:    
    aprovados = self.arquivo_data_frame['Aprovado'] == True
    df_aprovados = self.arquivo_data_frame[aprovados]
    print(f'Lista dos Aprovados\n {df_aprovados}') 
    
    df_aprovados.to_csv(nome_arquivo_destino, sep=';')
    df_aprovados.replace({'Notas':7.0}, 8.0, inplace=True)
    print(f'Aprovados: {df_aprovados}')

if __name__ == "__main__":
  arquivo_csv = Arquivo('alunos.csv', ';', '.')
  arquivo_csv.manipula_arquivo()
  arquivo_csv.cria_arquivo('alunos_aprovados.csv')