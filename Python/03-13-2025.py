# https://docs.google.com/document/d/1H-7w1vtuNnfxdn9eZ246ihtW_m-gOzpGAw-hs06WM2U/edit?tab=t.0

'''frase = "Hello World"
print(frase)
print("Hello World")

palavra_1 = "Olá "
palavra_2 = "Mundo"
print(palavra_1 + palavra_2)

frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Caio"
print(frase)


frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("Diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("Diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("Diga a quinta palavra: ")
print(frase)


a = 6
b = 9
print(type(a))
soma = a + b
sub = a - b
mult = a * b
div = a/b
pot = a ** b
print(f"A soma entre {a} e {b} é {soma}")
print(f"A subtração entre {a} e {b} é {sub}")
print(f"A multiplicação entre {a} e {b} é {mult}")
print(f"A divisão entre {a} e {b} é {div}")
print(f"A potenciação entre {a} e {b} é {pot}")

nome = input("Diga seu nome: ")
print(f"Olá, {nome}! Bem vindo à calculadora")

a = float(input("Digite um número de sua preferência: "))
b = float(input("Digite outro número: "))
soma = a + b
sub = a - b
mult = a * b
div = a/b
pot = a ** b
print(f"A soma entre {a} e {b} é {soma}")
print(f"A subtração entre {a} e {b} é {sub}")
print(f"A multiplicação entre {a} e {b} é {mult}")
print(f"A divisão entre {a} e {b} é {div}")
print(f"A potenciação entre {a} e {b} é {pot}")

a = float(input("Digite um número de sua preferência: "))
b = float(input("Digite outro número: "))

print(f"O resultado de {a} > {b} é {a>b}")
print(f"O resultado de {a} < {b} é {a<b}")
print(f"O resultado de {a} >= {b} é {a>=b}")
print(f"O resultado de {a} <= {b} é {a<=b}")
print(f"O resultado de {a} = {b} é {a==b}")
print(f"O resultado de {a} != {b} é {a!=b}")


a = 2
b = 3

print("Testes com 'and':")
print(f"{a} < {b} and {a} != {b}, ou seja, {a < b} and {b != a} é igual a {a < b and b != a}")
print(f"{a} <= {b} and {a} == {b}, ou seja, {a <= b} and {b == a} é igual a {a <= b and b == a}")
print(f"{a} > {b} and {a} < {b}, ou seja, {a > b} and {b > a} é igual a {a > b and b < a}")
print(f"{a} >= {b} and {a} <= {b}, ou seja, {a >= b} and {b <= a} é igual a {a >= b and b <= a}")

a = 2
b = 3
print()
print("Testes com 'or':")
print(f"{a} < {b} or {a} != {b}, ou seja, {a < b} or {b != a} é igual a {a < b or b != a}")
print(f"{a} <= {b} or {a} == {b}, ou seja, {a <= b} or {b == a} é igual a {a <= b or b == a}")
print(f"{a} > {b} or {a} < {b}, ou seja, {a > b} or {a < b} é igual a {a > b or a < b}")
print(f"{a} >= {b} or {a} == {b}, ou seja, {a >= b} or {a == b} é igual a {a >= b or a == b}")

idade = int(input("Diga sua idade: "))
if idade >= 18:
    print("Aoba 🤠")
else:
    print("Pode não 😠")
'''


idoso = input("Você é idoso?\n->")
if idoso == 'sim':
    cartao = input("Você tem o cartão de idoso?\n->")
if idoso == 'sim' and cartao == 'sim':
    print("Pó estacionar 🛴🛴")
if idoso == 'sim' and cartao == 'sim':
    exit()
if idoso or cartao == 'não':
    deficiente = input("Você é deficiente?\n->")
if  deficiente == 'sim':
        cartaodef = input("Você tem o cartão de deficiente?\n->")
if deficiente == 'sim' and cartaodef == 'sim':
    print("Pó estacionar 🛴🛴")
else:
    print("rala carai 😠😠👊👊")