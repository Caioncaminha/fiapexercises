import pandas as pd

s = pd.Series([120, 130, 125, 127, 122, 127, 126, 600])

print(f'Média: {round(s.mean(), 2)}')
print(f'Mediana: {s.median()}')
print(f'Moda: {s.mode().tolist()}')
print(f'Variância Amostral: {round(s.var(ddof=0), 2)}')
print(f'DP Amostral: {s.std(ddof=1):.2f}')