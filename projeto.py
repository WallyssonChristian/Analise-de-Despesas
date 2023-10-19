import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get data from API
api_dadosabertosurl = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
resposta = requests.request("GET", api_dadosabertosurl, params={})
objetos = json.loads(resposta.text)
dados_df = pd.DataFrame(objetos['dados'])
# isolating useful data
dados_df = (dados_df[['id', 'nome', 'siglaPartido', "siglaUf"]])

def obter_total_despesas(id_deputado):
    api_dadosabertos_despesas = ("https://dadosabertos.camara.leg.br/api/v2/deputados/{}/despesas?ordem=ASC&ordenarPor=ano".format(id_deputado))
    despesas_resposta = requests.get(api_dadosabertos_despesas)
    despesas = despesas_resposta.json()
    despesas_df = pd.DataFrame(despesas['dados'])
    if despesas_df.empty:
        return {'id': id_deputado, 'despesas': ''}
    else:
        total_despesas = despesas_df['valorDocumento'].sum()
        return {'id': id_deputado, 'despesas': total_despesas}

resultados = dados_df['id'].apply(obter_total_despesas)
total_despesas_df = pd.DataFrame(resultados.tolist())
## Need optimization

# Merge DataFrames
dados_df = dados_df.merge(total_despesas_df)

# Number of deputies by each Uf
x = dados_df['siglaUf'].value_counts().index
y = dados_df['siglaUf'].value_counts().values
plt.figure(figsize=(15,5))
sns.barplot(x=x, y=y)
plt.plot()

# Number of deputies by each party
x = dados_df['siglaPartido'].value_counts().values
y = dados_df['siglaPartido'].value_counts().index
plt.figure(figsize = (20, 15))
sns.barplot(x=x, y=y)
plt.plot()

# sorting by despesas
despesas_df = dados_df.sort_values(by=['despesas', 'nome'], ascending=False)
# Drop NaN values
despesas_df = despesas_df[despesas_df['despesas'] != '']
despesas_df = despesas_df.dropna()

# Total spending per deputy
x = despesas_df['nome'].value_counts().head(10).index
y = despesas_df['despesas'].head(10).values
plt.figure(figsize = (20, 15))
sns.barplot(x=x, y=y)
plt.plot()

despesas_df.to_csv('despesas_deputados.csv')