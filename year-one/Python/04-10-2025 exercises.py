'''1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.'''

def nota_valida():
    nota = input("Digite uma nota entre zero e dez:\n")
    while not (nota.isnumeric() and 0 <= int(nota) and int(nota) <= 10):
        print("Valor inválido")
        nota = input("Digite uma nota entre zero e dez:\n")
    nota = int(nota)
    print(f"Sua nota é {nota}.")

## Outra forma de fazer com melhor conduta

def nota_valida_2():
    while True:
        nota = input("Diga sua nota: ")
        if nota.isnumeric():
            nota = int(nota)
            if nota > 0 and nota < 10:
                break
            print("Fora do intervalo")
        else:
            print("Tem que ser um numero!")

'''2- Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

def cadastro():
    nome = input("Diga seu nome: ")
    while len(nome) < 3:
        nome = input("Diga seu nome: ")
    
    while not(idade.isnumeric()):
        print("Idade inválida")
        idade = input("Diga sua idade: ")
    idade = int(idade)
    if idade < 0 or idade > 150:
        print("Idade inválida")
        idade = input("Diga sua idade: ")

    salario = input("Diga seu salário: ")
    while not salario.isnumeric():
        salario = int(salario)
        salario = input("Diga seu salário: ")
    
    sexo = input("Diga f ou m: ")
    while sexo != "f" and sexo != "m":
        sexo = input("Diga f ou m: ")
    
    e_c = input("Diga s,c,v ou d: ")
    while not (e_c == "s" or e_c == "c" or e_c == "v" or e_c == "d"):
        e_c = input("Diga s,c,v ou d: ")
    print(f"{nome}\n{idade}\n{salario}\n{sexo}\n{e_c}")

'''3- Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.'''

def populacao():
    pop_a = 80000
    pop_b = 200000
    anos = 0
    while pop_a <= pop_b:
        pop_a *= 1.03
        pop_b *= 1.015
        anos += 1
    print(f"A população A se tornará igual ou maior que a população B em {anos} anos.")

'''4- Faça um programa que leia 5 números e informe a soma e a média dos números.'''

def num_soma_med():
    c = 0
    soma = 0
    while c < 5:
        nota = input(f"Diga a {c+1} nota: ")
        while not nota.isnumeric():
            nota = input(f"Diga {c+1} nota: ")
        nota = int(nota)
        soma += nota
        c += 1
    media = soma/c
    print(media)

'''5- Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.'''

def num_inteiros():
    a = input("Diga o primeiro número: ")
    while not a.isnumeric():
        a = input("Diga o primeiro número: ")
    a = int(a)
    
    b = input("Diga o segundo número: ")
    while not b.isnumeric():
        b = input("Diga o segundo número: ")
    b = int(b)
    
    if b < a:
        aux = a
        a = b
        b = aux
    
    while a <= b:
        print(a, end=' ')
        a += 1

'''6- Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.'''

def login():
    nome = input("Diga seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    while nome == senha:
        print("Usuário e senha devem ser diferentes.")
        nome = input("Diga seu nome de usuário: ")
        senha = input("Digite sua senha: ")

'''7- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''

def tabuada():
    num = 1
    while num <= 10:
        mult = 1
        while mult <= 10:
            print(f"{num}*{mult} = {num*mult}")
            mult += 1
        num += 1
        print()

'''8- A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.'''

def fibonacci():
    a = 1
    b = 1
    i = 2
    while i < 7:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

'''9- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números ímpares.'''

def num_parimpar():
    i = 0
    pares = 0
    while i < 10:
        num = input("Digite um número:\n")
        while not num.isnumeric():
            num = input("Digite um número:\n")
        num = int(num)
        if num%2 == 0:
            pares += 1
        i += 1
    print(f"Você digitou {pares} pares e {i - pares} ímpares.")

'''10 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120'''

def fatorial():
    i = 1
    fatorial = 1
    while i < 10:
        i += 1
        fatorial *= i
    print(fatorial)

'''11 - Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

def num_primos():
    i = 2
    num = 137
    while True:
        print(f"{num}%{i} = {num%i}")
        if num %i == 0:
            print("Não é primo")
            break
        elif i >= num**(1/2):
            print("É primo")
            break
        i += 1

'''12 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que:
1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.'''

def salarios():
    salario = 1000
    ano = 1995
    taxa_i = 0.015
    while ano < 2000:
        taxa = 1 + taxa_i
        salario *= taxa
        ano += 1
    print(salario)

'''13 - Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.'''

def num_indet():
    intervalo_1 = 0
    intervalo_2 = 0
    intervalo_3 = 0
    intervalo_4 = 0
    while True:
        num = input("Digite um número:\n")
        while not num.isnumeric():
            num = input("Digite um número:\n")
        num = int(num)
        if num < 25:
            intervalo_1 += 1
        elif num < 50:
            intervalo_2 += 1
        elif num < 75:
            intervalo_3 += 1
        elif num < 100:
            intervalo_4 += 1
        else:
            print("Digite um número entre 0 e 100")
            
        if 0 <= num <= 100:
            continuar = input("Você quer continuar? s ou n\n")
            while not (continuar == "s" or continuar == "n"):
                continuar = input("Você quer continuar? s ou n\n")
            if continuar == "n":
                print(f"\nIntervalo 1: {intervalo_1}\nIntervalo 2: {intervalo_2}\nIntervalo 3: {intervalo_3}\nIntervalo 4: {intervalo_4}")
                print("Fim")
                break
            else:
                pass

'''14 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.'''

def eleicao():
    canditato_1 = 'João'
    canditato_2 = 'Maria'
    canditato_3 = 'Roberto'
    canditato_4 = 'Memphis'
    brancos = 'brancos'
    nulos = 'nulos'

    votos_1 = 0
    votos_2 = 0
    votos_3 = 0
    votos_4 = 0
    votos_brancos = 0
    votos_nulos = 0
    total = 0
    while True:
        opcao = input(f"Escolha:\n{canditato_1}\n{canditato_2}"
                    f"\n{canditato_3}\n{canditato_4}\n{brancos}"
                    f"\n{nulos} ")
        if not (opcao == canditato_1 or opcao == canditato_2 or
                    opcao == canditato_3 or opcao == canditato_4 or
                    opcao == brancos or opcao == nulos):
            print("Inválido!")
            continue

        if opcao == canditato_1:
            votos_1 += 1
        elif opcao == canditato_1:
            votos_2 += 1
        elif opcao == canditato_1:
            votos_3 += 1
        elif opcao == canditato_1:
            votos_4 += 1
        elif opcao == brancos:
            votos_brancos += 1
        else:
            votos_nulos += 1
        total += 1
        proxima = input("Quer continuar? (s/n)\n->")
        while not (proxima == 's' or proxima == 'n'):
            proxima = input("Quer continuar? (s/n)\n->")
        if proxima == 'n':
            break

    print(f"{canditato_1} - {votos_1}\n{canditato_2} - {votos_2}\n"
        f"{canditato_3} - {votos_3}\n{canditato_4} - {votos_4}\n"
        f"{brancos} - {votos_brancos}\n{nulos} - {votos_nulos}\n")
    print(f"Porcentagem de nulos sobre o total: {votos_nulos*100/total:.2f}")
    print(f"Porcentagem de brancos' sobre o total: {votos_brancos*100/total:.2f}")