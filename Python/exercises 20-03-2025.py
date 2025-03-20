'''Exercício 1:
    Escreva um programa para ler 2 valores (diferentes) e escrever o maior deles'''

'''print("Escreva dois números diferentes para uma comparação\n")
a = int(input("Primeiro número:\n"))
b = int(input("Segundo número\n"))

if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("Números DIFERENTES")'''

'''Exercício 2
    Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá
    votar ou não vota este ano (desconsidere meses)'''

'''print("Digite seu ano de nascimento:\n")
ano = int(input(""))
idade = 2025 - ano
if idade >= 18:
    print("Você pode votar este ano.")
else:
    print("Você não pode votar este ano")'''

'''Exercício 3
    Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é
    o numero "1234". Devem ser impressas as seguintes mensagens:
        ACESSO PERMITIDO caso a senha seja válida.
        ACESSO NEGADO caso a senha seja inválida.'''

'''print("Digite a senha (quatro dígitos):\n")
senha = int(input(""))
if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")'''

'''Exercício 4
    As maçãs custam R$0,30 cada se forem compradas menos do que uma dúzia (12), e R$0,25 se forem compradas
    pelo menos uma dúzia (12). Escreva um programa que leia o número de maçãs compradas, calcule e escreva
    o valor total da compra'''

'''print("Quantas maçãs você quer comprar? Comprando uma dúzia (12) ou mais você ganha um desconto.")
macas = int(input(""))
if macas <= 0:
    print("Informe um valor válido de maçãs")
if macas >= 12:
    print(f"Você está comprando {macas}, o valor total é {macas * 0.25}R$")
else:
    print(f"Você está comprando {macas}, o valor total é {macas * 0.3}R$")'''

'''Exercício 5
    Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
    escrevê-los em ordem crescente'''

'''a = int(input("Digite o primeiro número"))
b = int(input("Digite o segundo número"))
c = int(input("Digite o terceiro número"))'''

'''Exercício 6
    Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1feminino, 2 masculino) de
    uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
    - para homens: (72.7 * Altura) - 58
    - para mulheres: (62.1 * Altura) - 44.7'''

'''sexo = int(input("Informe seu sexo (1 = feminino, 2 = masculino):\n"))
altura = float(input("Informe sua altura (metros):\n"))
idealmasc = format((72.7 * altura) - 58)
idealfemi = format((62.1 * altura) - 44.7)
if sexo == 1:
    print(f"Seu peso ideal é: {idealfemi}")
else:
    print(f"Seu peso ideal é: {idealmasc}")'''

'''Exercício 7
    Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
    Calcular e imprimir o seguinte:
    - Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área.
    - Se o número de lados for igual a 4 escrever QUADRADO e o valor da área.
    - Se o número de lados for igual a 5 escrever PENTÁGONO e o valor da área.'''
print("Escreva um número de lados de um polígono regular e a medida de seus lados")
lados = int(input("Quantidade de lados:\n"))
area = int(input("Medida de um de seus lados:\n"))
if lados == 3:
    print(f"Você escolheu um TRIÂNGULO com área igual a {format(area * (area * 0.5)/2)}")
if lados == 4:
    print()

