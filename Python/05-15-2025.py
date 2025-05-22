'''ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)

vinho1 = 'Pérgola'
vinho2 = 'Sangue de Boi'
vinho3 = 'Cantinho do Vale'
preco1 = 10
preco2 = 20
preco3 = 30
qtd1 = 0
qtd2 = 0
qtd3 = 0


idade = 2025 - ano
if idade < 18:
    print("Que feio, vô conta p sua mãe!")
else:
    endereco = input("Diga seu endereço: ")
    while True:
        escolha = input(f"Esses são nossos vinhos: \n{vinho1} - {preco1}\n"
                        f"\n{vinho2} - {preco2}\n{vinho3} - {preco3}"
                        f"Qual você quer? \n")
        while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
            print(f"{escolha} não é uma opção válida")
            escolha = input(f"Esses são nossos vinhos: \n{vinho1} - {preco1}\n"
                        f"\n{vinho2} - {preco2}\n{vinho3} - {preco3}"
                        f"Qual você quer? \n")
        qtd = input(f"Quantas garrafas de {escolha} você quer? \n ->")
        while not qtd.isnumeric():
            print("Inválido")
            qtd = input(f"Quantas garrafas de {escolha} você quer? \n ->")
        qtd = int(qtd)
        if escolha == vinho1:
            preco = preco1
            qtd1 += qtd
        elif escolha == vinho2:
            preco = preco2
            qtd2 += qtd
        else:
            preco = preco3
            qtd3 += qtd
        valortotal += qtd*preco
        continuar = input("Você quer continuar comprando? (s/n)\n ->")
        while not (continuar = 's' or continuar == 'n'):
            continuar = input("Você quer continuar comprando? (s/n)\n ->")
        if continuar == 'n':
            break
    frete = 10
    if valortotal >= 500:
        print("Frete Grátis!")
        frete = 0
    valortotal += frete
    print(f"Obrigado por comprar conosco! Você comprou \n{qtd1} - {vinho1}"
          f"\n {qtd2} - {vinho2}\n {qtd3} - {vinho3}\n Totalizando R${valortotal}"
          f"e seu pedido será entregue em {endereco}.")

for i in range(10):
    print(i)
    
for i in range(1,10,3):
    print(i) 

for i in range (20,10,-2):
    print(i)


for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range (1,11):
        print(f"{i}*{j} = {i*j}")
    print()
#2 códigos iguais, usando for e while respectivamente
i = 1
while i < 11:
    j = 1
    print(f"Tabuada do {i}:")
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j += 1
    i += 1
    print()
'''

'''lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    print(elem)
print()
for i in range(len(lista)):
    print(f"lista[{i}] = lista {lista[i]}")
'''

'''lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    elem = 1
print(lista)
print()
for i in range(len(lista)):
    lista[i] = 1
print(lista)

def lista():
    profs = ['Danilo', 'André', 'Gabi', 'Celso', 'Yan', 'Lucas', 'Luís']
    materias = ['Python', 'Historinha', 'Enrolação', 'Matemática', 'Arduino', 'Front', 'Web']
    for i in range(len(profs)):
        print(f"O/a {profs[i]} DÁ {materias[i]}")
        
lista()


def notas():
    alunos = ['Lucas Sena', 'Rhariel', 'Sara', 'Isabela', 'Lucas Zago']
    notas = [8,8.5,6,4,1]

    for i in range(len(alunos)):
        if notas[i] >= 6:
            print(f"{alunos[i]} aprovado!")
        else:
            print(f"{alunos[i]} reprovaram!")

notas()

def numeros():
    numeros = [4, 3, 7, 9, 2, 1, 6, 0, 5, 8]
    
    pares = 0
    for i in numeros:
        if i % 2 == 0:
            pares += 1
    print(f"Existem {pares} pares")       

    num = 0
    for i in numeros:
        num += numeros[i]
    print(f"A soma total é: {num}")
    
    media = 0
    for i in numeros:
        media = numeros[i] / len(numeros)
    print(f"A média é {media}.")

numeros()
'''

'''
def numusu():
    lista = []
    for i in range(10):
        pedido = input(f"Escreva o {i+1} número: ")
        while not pedido.isnumeric():
            pedido = input(f"Escreva o {i+1} número: ")
        pedido = int(pedido)
        lista.append(pedido)
    print(lista)
        
numusu()
'''

'''
def maior():
    lista = [4, 3, 7, 9, 2, 1, 6, 0, 5, 8]
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    print(maior)
    
maior()
'''

def posicao():
    preco = [600, 50, 80, 1000000, 5]
    carros = ['Mustang', 'Up', 'Gol', 'POLINHO TURBÃO MANUAL', 'Uno']
    indice_maior = 0
    maior = preco[0]
    for i in range(len(preco)):
        if preco[i] > maior:    
            maior = preco[i]
            indice_maior = i
    print(f"O carro mais caro é o {carros[indice_maior]}")
posicao()