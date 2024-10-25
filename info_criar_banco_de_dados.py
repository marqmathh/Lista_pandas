import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text
import pandas as pd

# SELECT: especifica quais colunas devem ser selecionadas na consulta.
# FROM: especifica as tabelas do banco de dados que devem ser consultadas.
# WHERE: filtra os resultados da consulta com base em uma ou mais condições especificadas.
# ORDER BY: classifica os resultados da consulta em ordem crescente ou decrescente com base em uma ou mais colunas.
# GROUP BY: agrupa os resultados da consulta com base em uma ou mais colunas.
# LIMIT: limita o número de linhas retornadas pelos resultados da consulta.

engine = create_engine('sqlite:///:memory:') # Cria banco de dados

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'
dados = pd.read_csv(url)

dados.to_sql('clientes', engine, index=False) # transformando os arquivos csv no formato do banco de dados

# inspector = inspect(engine) # inspecionar o banco de dados

# print(inspector.get_table_names()) # ver o nome das tabelas no banco de dados

# query = 'SELECT * FROM clientes WHERE Categoria_de_renda="Empregado"' # faz a seleção
# empregados = pd.read_sql_query(query, engine)  # mostra a seleção na tabela
# print(empregados) # exibe os dados da tabela clientes onde a categoria de renda é empregado

# empregados.to_sql('empregados', con=engine, index=False)  # adicionando ao sql

# print(pd.read_sql_table('empregados',engine)) # mostra toda a tabela
# print(pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']))  # mostra apenas as colunas desejadas

# query = 'SELECT * FROM clientes' # deixa sem seleção
# print(pd.read_sql(query, engine)) # mostra toda a tabela
query = text('DELETE FROM clientes WHERE ID_Cliente=5008804')  # deleta a linha
with engine.connect() as conn:  # faz a conexão
    conn.execute(query)   # executa a query

query = text('UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808')   # atualiza a linha
with engine.connect() as conn:   # faz a conexão
    conn.execute(query)    # executa a query

print(pd.read_sql_table('clientes', engine))  # mostra toda a tabela

