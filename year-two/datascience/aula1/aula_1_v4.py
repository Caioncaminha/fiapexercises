# case 2
# amostra (10 dias úteis): [23, 25, 21, 20, 22, 60, 24, 23, 21, 22]
# 1) Moda existe? O que ela diz?
# 2) Compare média e mediana: o que o dia com 60 tickers faz com a média?
# 3) Calcule variância amostral e desvio padrão amostral e explique o que isso revela sobre previsibilidade

import pandas as pd

dados = [23, 25, 21, 20, 22, 60, 24, 23, 21, 22]
serie = pd.Series(dados)
# 1)
moda = serie.mode().tolist()
print(f'Moda: {moda}')

# 2)
media = serie.mean()
mediana = serie.median()
print(f'Média: {media}')
print(f'Mediana: {mediana}')

# 3)
variancia = serie.var(ddof=1)
desvio_padrao = serie.std(ddof=1)
print(f'Variância amostral: {round(variancia, 2)}')
print(f'Desvio padrão amostral: {round(desvio_padrao, 2)}')
