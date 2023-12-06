# código de geração do gráfico 
import pandas as pd
import seaborn as sns


gasolina_df = pd.read_csv('gasolina.csv', sep=',')

## gerando o gráfico

with sns.axes_style('whitegrid'):

  gráfico = sns.lineplot(data = gasolina_df, x='dia', y = 'venda', palette='dark')
  gráfico.set(title='Preço da gasolina por dia')