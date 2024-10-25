import pandas as pd

# https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/edit?usp=sharing
# 1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog' #ID da  planilha no google sheets
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'  #url da planilha
dados_co2_sheets = pd.read_csv(url)  # Ler a planilha do google sheets


sheet_name = 'emissoes_percapita'   #nome da aba
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'   #url da planilha
percapita_sheets = pd.read_csv(url_percapita)   # Ler a planilha do google sheets

print(percapita_sheets.head())