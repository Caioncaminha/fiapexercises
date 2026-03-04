import pandas as pd
# calcular média, mediana, moda, variância amostral, desvio padrão amostral
# amostra = 98, 105, 101, 99, 110, 500, 103, 97, 102, 108

dados = [98, 105, 101, 99, 110, 500, 103, 97, 102, 108]
serie = pd.Series(dados)

# 1)
# Média: 142.3
# Mediana: 102.5
# Moda: [97, 98, 99, 101, 102, 103, 105, 108, 110, 500]
# Variância amostral: 15813.79
# Desvio padrão amostral: 125.75

media = serie.mean()
mediana = serie.median()
moda = serie.mode().tolist()
variancia = serie.var(ddof=1)
desvio_padrao = serie.std(ddof=1)

# 2) Mediana

print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Variância amostral: {round(variancia, 2)}')
print(f'Desvio padrão amostral: {round(desvio_padrao, 2)}')

# 3) Se o SLA diz "típico < 120ms", está ok.

if mediana < 120:
    print('\nEstá ok.')
else:
    print('\nNão está ok.')