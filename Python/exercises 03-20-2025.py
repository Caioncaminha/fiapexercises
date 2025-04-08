'''Exercício 1:
        Escreva um programa para ler 2 valores (diferentes) e escrever o maior deles'''

def maior_numero1_():
    print("Escreva dois números diferentes para uma comparação\n")
    a = int(input("Primeiro número:\n"))
    b = int(input("Segundo número\n"))

    if a > b:
        print(f"{a} é maior que {b}")
    elif b > a:
        print(f"{b} é maior que {a}")
    else:
        print("Números DIFERENTES")



'''Exercício 2
    Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá
    votar ou não vota este ano (desconsidere meses)'''

def votacao():
    ano = int(input("Digite seu ano de nascimento"))
    idade = 2025 - ano
    if idade >= 18:
        print("Você pode votar este ano.")
    else:
        print("Você não pode votar este ano")



'''Exercício 3
Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é
o numero "1234". Devem ser impressas as seguintes mensagens:
    ACESSO PERMITIDO caso a senha seja válida.
    ACESSO NEGADO caso a senha seja inválida.'''

def senha():
    senha = "1234"
    tentativa = input("Digite a senha:\n")
    if senha == tentativa:
        print("ACESSO PERMITIDO")
    else:
        print("ACESSO NEGADO")



'''Exercício 4
    As maçãs custam R$0,30 cada se forem compradas menos do que uma dúzia (12), e R$0,25 se forem compradas
    pelo menos uma dúzia (12). Escreva um programa que leia o número de maçãs compradas, calcule e escreva
    o valor total da compra'''

def macas():
    print("Quantas maçãs você quer comprar? Comprando uma dúzia (12) ou mais você ganha um desconto.")
    macas = int(input(""))
    if macas <= 0:
        print("Informe um valor válido de maçãs")
    if macas >= 12:
        print(f"Você está comprando {macas}, o valor total é {macas * 0.25}R$")
    else:
        print(f"Você está comprando {macas}, o valor total é {macas * 0.3}R$")



'''Exercício 5
    Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
    escrevê-los em ordem crescente'''

def ordem_crescente():
    a = int(input("Primeiro valor:\n"))
    b = int(input("Segundo valor:\n"))
    c = int(input("Terceiro valor:\n"))
    if a < b < c:
        print(f"{a}, {b}, {c}")
    elif a < c < b:
        print(f"{a}, {c}, {b}")
    elif b < a < c:
        print(f"{b}, {a}, {c}")
    elif b < c < a:
        print(f"{b}, {c}, {a}")
    elif c < a < b:
        print(f"{c}, {a}, {b}")
    elif c < b < a:
        print(f"{c}, {b}, {a}")
    else:
        print("Valores inválidos")



'''Exercício 5
    Exercício 5 feito da maneira "corrigida" pelo professor (não otimizada)'''

def ordem_crescente_corrigido():
    a = int(input("Primeiro valor:\n"))
    b = int(input("Segundo valor:\n"))
    c = int(input("Terceiro valor:\n"))
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a, b, c)



'''Exercício 5
    Exercício 5 feito da maneira corrigida pelo professor, otimizada'''

def ordem_crescente_corrigido2():
    a = int(input("Primeiro valor:\n"))
    b = int(input("Segundo valor:\n"))
    c = int(input("Terceiro valor:\n"))

    if a > b and a > c:
        aux = a
        a = c
        c = aux
    elif b > c:
        aux = b
        b = c
        c = aux
    if b < a:
        aux = a
        a = b
        b = aux
    print(a,b,c)



'''Exercício 5
    Exercício 5 feito de uma maneira diferente, utilizando"sort"'''

def ordem_crescente_corrigido3():
    a = int(input("Primeiro valor:\n"))
    b = int(input("Segundo valor:\n"))
    c = int(input("Terceiro valor:\n"))
    lista = [a, b, c]
    lista.sort()
    print(lista)



'''Exercício 6
    Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1feminino, 2 masculino) de
    uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
    - para homens: (72.7 * Altura) - 58
    - para mulheres: (62.1 * Altura) - 44.7'''

def peso_ideal():
    sexo = int(input("Informe seu sexo (1 = feminino, 2 = masculino):\n"))
    altura = float(input("Informe sua altura (metros):\n"))
    idealmasc = format((72.7 * altura) - 58)
    idealfemi = format((62.1 * altura) - 44.7)
    if sexo == 1:
        print(f"Seu peso ideal é: {idealfemi}")
    else:
        print(f"Seu peso ideal é: {idealmasc}")



'''Exercício 7 (NÃO OTIMIZADO)
    Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
    Calcular e imprimir o seguinte:
    - Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área.
    - Se o número de lados for igual a 4 escrever QUADRADO e o valor da área.
    - Se o número de lados for igual a 5 escrever PENTÁGONO e o valor da área.'''

def poligonos():
    print("Escreva um número de lados de um polígono regular e a medida de seus lados")
    lados = int(input("Quantidade de lados:\n"))
    area = float(input("Medida de um de seus lados:\n"))
    if lados == 3:
        print(f"Você escolheu um TRIÂNGULO com área igual a {format(area * (area * 0.5)/2)}")
    elif lados == 4:
        print(f"Você escolheu um QUADRADO com área igual a {format(area * area)}")
    elif lados == 5:
        print(f"Você escolheu um PENTÁGONO com área igual a {format(1.72 * area ** 2)}")
    else:
        print("Escolha um número de lados válido (3, 4 ou 5)")



'''Exercício 8 (NÃO OTIMIZADO)
    Acresente as seguintes mensagens à solução do exercício anterior conforme o caso.
    - Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.'
    - Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.'''

def poligonos2():
    print("Escreva um número de lados de um polígono regular e a medida de seus lados")
    lados = int(input("Quantidade de lados:\n"))
    area = float(input("Medida de um de seus lados:\n"))
    if lados == 3:
        print(f"Você escolheu um TRIÂNGULO com área igual a {format(area * (area * 0.5)/2)}")
    elif lados == 4:
        print(f"Você escolheu um QUADRADO com área igual a {format(area * area)}")
    elif lados == 5:
        print(f"Você escolheu um PENTÁGONO com área igual a {format(1.72 * area ** 2)}")
    else:
        print("Escolha um número de lados válido (3, 4 ou 5)")
    if lados < 3:
        print("NÃO É UM POLÍGONO")
    elif lados > 5:
        print("POLÍGONO NÃO IDENTIFICADO")



'''Exercício 9
    Escreva um programa para ler 3 valores inteiros e escrever o maior deles.'
    Considere que o usuário não informará valores iguais.'''

def maior_numero_2():
    a = int(input("Digite o primeiro número\n"))
    b = int(input("Digite o segundo número\n"))
    c = int(input("Digite o terceiro número\n"))
    if a > b and a > c:
        print(f"O número {a} é o maior")
    elif b > c:
        print(f"O número {b} é o maior")
    else:
        print(f"O número {c} é o maior")



'''Exercício 10
    Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é equilátero, isósceles ou escaleno.
    Sendo que:
    - Triângulo Equilátero: possui os 3 lados iguais.
    - Triângulo Isósceles: possui 2 lados iguais.
    - Triângulo Escaleno: possui 3 lados diferentes.'''

def triangulos():
    print("Digite as medidas dos lados de um triângulo")
    a = float(input("Digite o primeiro lado\n"))
    b = float(input("Digite o segundo lado\n"))
    c = float(input("Digite o terceiro lado\n"))
    if a == b and a == c:
        print("Este triângulo é equilátero")
    elif a == b or a == c or b == c:
        print("Este triângulo é isósceles")
    else:
        print("Este triângulo é escaleno")



'''Exercício 11
    Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo
    ou Obtusângulo.
    Sendo que:
    - Triângulo Retângulo: possui um ângulo reto (igual a 90º).
    - Triângulo Obtusângulo: possui um ângulo obtuso (maior que 90º).
    - Triângulo Acutângulo: possui três ângulos agudos (menor que 90º).'''

def angulos_triangulos():
    print("Digite os ângulos de um triângulo")
    a = int(input("Digite o primeiro ângulo\n"))
    b = int(input("Digite o segundo ângulo\n"))
    c = int(input("Digite o terceiro ângulo\n"))
    if a + b + c == 180:
        if a == 90 or b == 90 or c == 90:
            print("Este triângulo é retângulo.")
        elif a > 90 or b > 90 or c > 90:
            print("Este triângulo é obtusângulo.")
        else:
            print("Este triângulo é agudo.")
    else:
        print("Isso não é um triângulo")
