import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# print(dados) # exibe todos os dados
# print(dados.head()) # exibe os primeiros  5 registros
# print(dados.tail()) # exibe os últimos 5 registros
# print(type(dados)) # exibe o tipo dos dados
# print(dados.shape) # exibe a quantidade de  linhas e colunas
# print(dados.columns)  # exibe as colunas
# print(dados.info()) # exibe tipo de dados por colunas

# print(dados['Tipo']) # exibe tipo de dados da coluna especifica
# print(dados[['Tipo','Quartos']]) # exibe tipo de dados das colunas especificas
# print(dados['Valor'].mean()) # exibe a média dos valores da coluna especifica
# print(dados.groupby('Tipo').mean(numeric_only=True))  # exibe a média dos valores da coluna especifica agrupada pelo tipo
# print(dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))  # exibe a média dos valores da coluna especifica agrupada pelo tipo e o sort_values classifica do menor para o maior

# df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor') # criei uma váriavél para plotar no gráfico
# df_preco_tipo.plot(kind='barh', figsize=(14, 10), color ='purple') #  plotar o gráfico
# plt.title('Média de Valores por Tipo') # titulo gráfico
# plt.xlabel('Valor Médio') # titulo eixo x
# plt.ylabel('Tipo') # titulo eixo y
# plt.show() # mostra o gráfico

# print(dados.Tipo.unique())  # mostra os dados da coluna (sem duplicatas)
# imoveis_comerciais = ['Conjunto Comercial/Sala', 
                    #   'Prédio Inteiro', 'Loja/Salão', 
                    #   'Galpão/Depósito/Armazém', 
                    #   'Casa Comercial', 'Terreno Padrão',
                    #   'Loja Shopping/ Ct Comercial',
                    #   'Box/Garagem', 'Chácara',
                    #   'Loteamento/Condomínio', 'Sítio',
                    #   'Pousada/Chalé', 'Hotel', 'Indústria']
# print(dados.query('@imoveis_comerciais in Tipo'))  # exibe os (imoveis comerciais) da coluna (Tipo)
# print(dados.query('@imoveis_comerciais not in Tipo'))  # exibe os itens sem os (imoveis comerciais) da coluna (Tipo)
# df = dados.query('@imoveis_comerciais not in Tipo') # criei uma váriavél com a condicional
# print(df.Tipo.unique()) # mostra os dados da coluna (sem duplicatas)

# df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor') # criei uma váriavél para plotar no gráfico
# df_preco_tipo.plot(kind='barh', figsize=(14, 10), color ='purple') #  plotar o gráfico
# plt.title('Média de Valores por Tipo') # titulo gráfico
# plt.xlabel('Valor Médio') # titulo eixo x
# plt.ylabel('Tipo') # titulo eixo y
# plt.show() # mostra o gráfico

# print(df.Tipo.value_counts()) # exibe a quantidade de cada (tipo de imóvel)
# print(df.Tipo.value_counts(normalize=True)) # exibe a quantidade de cada (tipo de imóvel) em porcentagem %
# print(df.Tipo.value_counts(normalize=True).to_frame()) # transforma em dataframe (melhor vizualização na web)
# df_counts = df.Tipo.value_counts(normalize=True).to_frame(name='Porcentagem') # Criei a váriaivel e dei um nome para a coluna de dataframe
# df_percentual_tipo = df_counts.sort_values(by='Porcentagem', ascending=True) # classifiquei a coluna do datafram do menor para o maior e criei uma váriavel

# df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color ='green', edgecolor='black')  #  plotar o gráfico
# plt.title('') # titulo gráfico
# plt.xlabel('Tipos') # titulo eixo x
# plt.ylabel('Percentual') # titulo eixo y
# plt.show() # mostra o gráfico

# print(df.query('Tipo == "Apartamento"')) # exibe os apartamentos da coluna (Tipo)
# df = df.query('Tipo == "Apartamento"') # criei uma váriavél com a condicional

# print(df.isnull()) # exibe os valores nulos da váriavel (True = nulo)
# print(df.isnull().sum()) # exibe a quantidade de valores nulos da váriavel
# df = df.fillna(0) # preenche os valores nulos com 0
# print(df.query('Valor == 0 | Condominio == 0'))  # exibe os valores 0  da coluna (Valor e Condominio)
# print(df.query('Valor == 0 | Condominio == 0').index) # exibe as linhas que estão vazias
# registros_a_remover = df.query('Valor == 0 | Condominio == 0').index  # criei uma váriavél com as linhas que estão vazias
# df.drop(registros_a_remover, axis=0, inplace=True) # aqui eu removi as linhas da tabela, axis (0 remover linhas, 1 remover colunas), inplce já adiciona à váriavel  df
# df.drop('Tipo', axis=1, inplace=True) # Removi uma coluna

# selecao1 = df['Quartos'] == 1 # mostra as linhas que em que o quarto é igual a 1  
# selecao2 = df['Valor'] < 1200 # mostra as linhas que estão menor que 1200
# selecao_final = (selecao1) & (selecao2) # estou fazendo duas seleções
# df_1 = df[selecao_final]  # criei uma váriavél com as seleções
# selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70) # faz vários filtros ao mesmo tempo
# df_2 = df[selecao] # criei uma váriaivel com a seleção

# df.to_csv('dados_apartamentos.csv', index=False, sep=';') # salvei a nova tabela em csv, index = false é para não criar uma coluna numerica no começo do arquivo, sep para o separador ficar com ';'
# csvv = pd.read_csv('dados_apartamentos.csv') # criando váriavel do arquivo
# print(csvv) # lendo o arquivo

# dados['Valor por mes'] = dados['Valor'] + dados['Condominio']  # criei uma nova coluna com a soma de valor e condominio
# dados['Valor por ano'] = (dados['Valor por mes'] * 12) + dados['IPTU']   # criei uma nova coluna com a soma de valor por mes * 12 + iptu
# dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + dados['Quartos'].astype(str) + ' quarto(s) ' + ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.' #  criei uma nova coluna com a descrição dos imoveis de números e strings
# dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")  # criei uma nova coluna com a aplicação de uma função lambda para verificar se possi suite

print(dados.head())

