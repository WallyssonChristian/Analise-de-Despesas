# Análise de Despesas de Deputados Brasileiros

Este projeto utiliza a API de Dados Abertos da Câmara dos Deputados para analisar as despesas de deputados brasileiros. A análise inclui a contagem de deputados por estado e por partido, bem como a classificação dos deputados com base em suas despesas totais.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado as bibliotecas Python necessárias. Você pode instalá-las executando:

```bash
pip install requests pandas seaborn matplotlib wordcloud
pip install git+https://github.com/amueller/word_cloud.git
```

## Configuração

1. Clone o repositório:
```bash
git clone https://github.com/WallyssonChristian/Analise-de-Despesas
cd Analise-de-Despesas
```
2. Execute o Script Python:
```bash
projeto.py
```
3. Os resultados da análise serão salvos em um arquivo CSV chamado despesas_deputados.csv.

## Resultados da Análise
- Número de Deputados por Estado
- Número de Deputados por Partido
- Total de Despesas por Deputado (Top 10)

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.
