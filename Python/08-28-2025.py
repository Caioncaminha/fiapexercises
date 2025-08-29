def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

criar_matriz(3,4)

def matriz_diagonal(linhas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(linhas):
            if i == j:
                linha.append("x")
            else:
                linha.append('.')
        matriz.append(linha)
    return matriz

matriz_diagonal(5)

def matriz_diagonal_prof(tamanho):
    matriz = criar_matriz(tamanho,tamanho)
    for i in range(tamanho):
        matriz[i][i] = 'x'
    return matriz