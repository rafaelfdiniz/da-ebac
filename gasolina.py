# código de geração do gráfico 
import pandas as pd
import seaborn as sns


gasolina_df = pd.read_csv('gasolina.csv', sep=',')

## gerando o gráfico

with sns.axes_style('whitegrid'):

  gráfico = sns.lineplot(data = gasolina_df, x='dia', y = 'venda', palette='deep')
  gráfico.set(title='Gráfico Preço da Gasolina X Dia')