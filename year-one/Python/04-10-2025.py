'''

i = 0
pares = 0
num = int(input(f"Diga o {i+1} número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1


i = 0
pares = 0

while i < 5:
    num = int(input(f"Diga o {i+1} número: "))
    if num%2 == 0:
        pares = pares + 1
    i = i + 1
print(f"Você digitou {pares} números pares e {i - pares} números ímpares.")

# i = i + 1 ->> i += 1

t = 0
senha = "1234"
while t < 3:
    tentativa = input("Digite a senha: \n")
    t = t + 1
    if tentativa == senha:    
        print("ACESSO PERMITIDO")
        t = 3
    else:
        print("ACESSO NEGADO")
        
# t = t + 1 ->> t += 1


sexo = input("Escolha seu sexo (masculino ou feminino): \n")
while sexo != "masculino" and sexo != "feminino":
    #print("Escolha um sexo válido")
    sexo = input("Escolha seu sexo (masculino ou feminino): \n")
#print("Prossiga.")

sexo = input("Escolha seu sexo (masculino ou feminino): \n")
while not (sexo == "masculino" or sexo == "feminino"):
    #print("Escolha um sexo válido")
    sexo = input("Escolha seu sexo (masculino ou feminino): \n")
#print("Prossiga.")


num = input("Digite um número: \n")
print(type(num))
while not (num.isnumeric()):
    num = input("Digite um número: \n")
num = int(num)
print(type(num))
'''