import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'
dados_mercado = pd.read_csv(url)

url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'
dados_ponto_virgula = pd.read_csv(url_2)
dados_sem_virgula = pd.read_csv(url_2, sep=';') # com separador
dados_primeiras_linhas = pd.read_csv(url,nrows=5) # Mostrar primeiras 5 linhas
dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth','Income']) # mostra apenas as colunas escolhidas
dados_selecao = pd.read_csv(url, usecols=[0,1,4]) #mostra as colunas (1, 2 , 5) do arquivo csv

dados_selecao.to_csv('clientes_mercado.csv', index=False)  # Salvar em um arquivo csv

clientes_mercado = pd.read_csv('clientes_mercado.csv')
print(clientes_mercado.head())