import pandas as pd

dados_pacientes = pd.read_json('pacientes.json') # arquivo JSON normal
dados_pacientes_2 = pd.read_json('pacientes_2.json') # arquivo JSON bugado
df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes']) # correção do arquivo JSON  bugado

print(df_normalizado)

df_normalizado.to_json('historico_pacientes_normalizado.json')