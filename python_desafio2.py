import pandas as pd

df_vacinados = pd.read_csv('vacinados_CERTO CERTO.csv')

df_vacinados_1 = df_vacinados.loc[(df_vacinados['sexo'] == 'FEMININO') & (df_vacinados['idade'] >= 60) & ((df_vacinados['raca_cor'] == 'PRETA')|(df_vacinados['raca_cor'] == 'PARDA')) & (df_vacinados['municipio'] == 'RECIFE')]
df_vacinados_2 = df_vacinados.loc[(df_vacinados['sexo'] == 'MASCULINO') & ((df_vacinados['data_vacinacao'].str.contains('11')))]
print(df_vacinados_1)
print(df_vacinados_2)
