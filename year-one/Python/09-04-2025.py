def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def matriz_x(linhas, colunas):
    mat = criar_matriz(linhas, colunas)
    for i in range(colunas):
        mat[0][i] = 'x'
        mat[linhas - 1][i] = 'x'
        mat[i][0] = 'x'
        mat[i][colunas - 1] = 'x'
    return mat

def matriz_bordas(linhas, colunas):
    mat = criar_matriz(linhas,colunas)
    for i in range(colunas):
        mat[0][i] = 'x'
        mat[linhas - 1][i] = 'x'
        for j in range(linhas):
            mat[j][0] = 'x'
            mat[j][colunas - 1] = 'x'
    return mat

