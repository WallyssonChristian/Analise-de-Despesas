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
dados_api_df = pd.DataFrame(objetos['dados'])

#dados_df.info()
id_deputado = "220539"
api_dadosabertos_despesas = ("https://dadosabertos.camara.leg.br/api/v2/deputados/{}/despesas?ordem=ASC&ordenarPor=ano".format(id_deputado))
despesas_resposta = requests.get(api_dadosabertos_despesas)
despesas = despesas_resposta.json()
despesas_df = pd.DataFrame(despesas['dados'])
despesas_df.info()