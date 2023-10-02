import pandas as pd

class Arquivo:
  nome_arquivo:str = None
  separador:str = None
  decimal_separator:str = None
  # constructor
  def __init__(self, nome_arquivo = None, separador = None, decimal_separator = None) -> None:
    self.nome_arquivo = nome_arquivo
    self.separador = separador
    self.decimal_separator = decimal_separator

  def manipula_arquivo(self):
    #print(f"Nome do arquivo: {self.nome_arquivo}")
    print(f"Separador: {self.separador}")
    print(f"Decimal: {self.decimal_separator}")
    df = pd.read_csv(self.nome_arquivo, sep = self.separador, decimal = self.decimal_separator)
    print(df)
    # Filtra os dez primeiros resultados
    #df.head(10)
    #df.isnull().sum()
    """
    # Tratamento para converter notas nulas em zero
    notas_nulas = {"Notas": 0,"Media": 0}
    df.fillna(value = notas_nulas, inplace = True)

    # Removendo com base no filtro Nome = Alice ou Nome = Carlos
    alunos_que_sairam = df.query('Nome == "Alice" | Nome == "Carlos"').index
    df.drop(alunos_que_sairam, axis=0, inplace=True)
    print(f'Sem os alunos que saíram\n {df}')

    aprovados = df['Aprovado'] == True
    df_aprovados = df[aprovados]
    print(f'Lista dos Aprovados\n {df_aprovados}')
    """

# Criando arquivo CSV
#df_aprovados.to_csv('alunos_aprovados.csv', sep=';')
#df_aprovados.replace({'Notas':7.0}, 8.0, inplace=True)
#print(f'Aprovados: {df_aprovados}')

if __name__ == "__main__":
  arquivo_csv = Arquivo('alunos.csv', ',', '.')
  arquivo_csv.manipula_arquivo()