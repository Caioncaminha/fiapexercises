'''
a = int(input("Primeiro valor:\n"))
b = int(input("Segundo valor:\n"))
c = int(input("Terceiro valor:\n"))

print(a,b,c)
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)
if b > c:
    aux = b
    b = c
    c = aux
print(a,b,c)
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)'''


'''lados = int(input("Diga a qtd de lados: "))
if lados < 3:
    print("Não é um polígono!!")
elif lados > 5:
    print("Polígono não identificado!")
else:
    medida = float(input("Diga a medida do lado: "))
    if lados == 3:
        forma = 'Triangulo'
        area = {format(medida * (medida * 0.5)/2)}
    elif lados == 4:
        forma = "Quadrado"
        area = {format(medida ** 2)}
    else:
        forma = "Pentágono"
        area = {format((1.72 * medida ** 2))}
    print(f"{forma} de área {area}")'''
    

dig = int(input("Digite um número com 3 casas: \n"))
if dig >=100 <=999:
    soma = dig
    print(sum)
else:
    print("Isso não é um número de 3 dígitos")