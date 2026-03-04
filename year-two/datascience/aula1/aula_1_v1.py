import statistics as st

lat_ms = [120, 130, 125, 128, 122, 127, 126, 600]

media = st.mean(lat_ms)
mediana = st.median(lat_ms)
moda = st.mode(lat_ms)
dp_amostral = round(st.stdev(lat_ms), 2) # amostral - (n-1)
var_amostral = round(dp_amostral ** 2, 2)

print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Variância Amostral: {var_amostral}')
print(f'DP Amostral: {dp_amostral}')