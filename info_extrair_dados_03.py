import matplotlib.pyplot as plt
import pandas as pd

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'
dados_co2 = pd.read_excel(url)
# print(pd.ExcelFile(url).sheet_names) # nome das abas da planilha

percapita = pd.read_excel(url, sheet_name='emissoes_percapita') #  leitura da aba 'emissoes_percapita'
fontes = pd.read_excel(url, sheet_name='fontes') #   leitura da aba 'fontes'

intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols= 'A:D')  # leitura da aba 'emissoes_C02' e seleção das colunas A até D
intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols= 'A:D', nrows=10) # leitura da aba 'emissoes_C02' e seleção das colunas A até D mostrando até a linha 10

percapita.to_excel('co2_percapita.xlsx', index=False)