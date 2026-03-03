'''
def funcao0(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

qtd = funcao0("Quantos números você vai colocar na lista?")

lista = []
while len(lista) < qtd:
    num = funcao0(f"Diga o {len(lista) +1} número: ")
    lista.append(num)
    print(lista)

def teste():
    def forca_opcao(msg, lista_opcoes):
        opcoes = '\n'.join(lista_opcoes)
        escolha = input(f"{msg}\n{opcoes}\n->")
        while not escolha in lista_opcoes:
            escolha = input (f"{msg}\n{opcoes}\n->")
        return escolha

    vinhos = ['Pérgola', 'Sangue de Boi', 'Salton']
    vinho = forca_opcao("Qual vinho você quer?", vinhos )
    print(f"Você escolheu o vinho {vinho}")
    opcoes = ['s', 'n']
    continuar = forca_opcao("Você quer continuar? ->", opcoes)
    print(f"Você disse {continuar}")
teste()
'''

'''
def media():
    def mediageral(lista_numeros):
        soma = 0
        for num in lista_numeros:
            soma += num
        media = soma/len(lista_numeros)
        return media
    lista = [5, 1, 4, 2, 0, 9]
    media = mediageral(lista)
    print(media)
    lista_2 = [1, 2, 3]
    media = mediageral(lista_2)
    print(media)
media()
'''

'''
def pares():
    def listapares(lista_numeros):
        pares = 0
        for num in lista_numeros:
            if num % 2 == 0:
                pares += 1
        return pares
    lista = [4, 3, 5, 6, 9, 1, 7, 8]
    print(listapares(lista))
pares()
'''

'''
def teste():

    def achar_maior(lista):
        indice_maior = 0
        maior = lista[indice_maior]
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                indice_maior = i
        return indice_maior
    
    carros = ['Up', 'Gol', 'POLINHO TURBÃO MANUAL', 'Uno', 'Celta']
    precos = [10, 20, 1000000, 100, 200]
    local_maior = (achar_maior(precos))
    print(f"O carro mais caro é o {carros[local_maior]} e custa {precos[local_maior]}")

teste()
'''

'''
def teste():
    
    def join(lista_str, sep):
        ajuntado = lista_str[0]
        for i in range(1, len(lista_str)):
            ajuntado += sep + lista_str[i]
        return ajuntado
    
    def forca_opcao(msg, lista_opcoes):
        opcoes = join(lista_opcoes, '\n')
        escolha = input(f"{msg}\n{opcoes}\n->")
        while not escolha in lista_opcoes:
            escolha = input (f"{msg}\n{opcoes}\n->")
        return escolha

    carros = ['Up', 'Gol', 'POLINHO TURBÃO MANUAL', 'Uno', 'Celta']
    precos = [10, 20, 1000000, 100, 200]
    escolha = forca_opcao("Qual carro você quer?", carros )

    def acha_index(lista, elem):
        for i in range(len(lista)):
            if lista[i] == elem:
                indice_escolha = i
                return i
            
    print(f"Você escolheu {escolha} e o preço desse carro é {acha_index(precos, )})")
    
teste()
'''

'''
def join(lista_str, sep):
    ajuntado = lista_str[0]
    for i in range(1, len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado 
'''
'''
def escolher(lista_carros, lista_precos):
    escolha = input(f'Escolha um carro:\n{join(lista_carros, '\n')}\n-> ')

    while escolha not in lista_carros:
        escolha = input(f'Inválido! Escolha um carro:\n{join(lista_carros, '\n')}\n-> ')

    index = 0
    preco = lista_precos[index]
    for i in range(len(precos)):
        if lista_carros[i] == escolha:
            index = i
            preco = lista_precos[i]

    return f'O carro selecionado foi {escolha} que custa {preco} mil reais.

carros = ['Up', 'Gol', 'Polinho Turbão Manual', 'Uno', 'Celta']
precos = [40, 50, 1000000, 100, 200]

carro_escolhido = escolher(carros, precos)
print(carro_escolhido)
'''