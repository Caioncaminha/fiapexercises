'''letra = input("Digite uma letra\n")

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Isso é uma vogal")
else:
    print("Isso não é uma vogal")

time = input('Diga para qual time você torce: \n')
if time == 'São Paulo':
    print('É... são paulo né.')
elif time == 'Palmeiras':
    print('Palmeiras?? Red flag.')
elif time == 'Corinthians':
    print('2005 foi roubado, parabéns pela série B')
else time == 'Santos':
    print('Parabéns pela série B, baixa taxa de natalidade, menino ney carrega')


salario = float(input("Digite seu salário.\n"))
if salario <= 0:
    print('Você não possui salário')
elif salario <= 2259.20:
    print('Você não precisa pagar imposto de renda. Seu salário é de:', format(salario - salario*(0/100)))
elif 2259.21 <= salario <= 2826.66:
    print('Sua alíquota de imposto de renda é 7.5%. Seu salário é de:', format(salario - salario*(7.5/100)))
elif 2826.67 <= salario <= 3751.05:
    print('Sua alíquota de imposto de renda é 15%. Seu salário é de:', format(salario - salario*(15/100)))
elif 3751.06 <= salario <= 4664.68:
    print('Sua alíquota de imposto de renda é 22.5%. Seu salário é de:', format(salario - salario*(22.5/100)))
elif 4664.69 <= salario:
    print('Sua alíquota de imposto de renda é 27.5. Seu salário é de:', format(salario - salario*(27.5/100)))


salario = float(input("Digite seu salário. \n"))
if salario <= 2259.20:
    aliquota = 0
elif salario <= 2826.66:
    aliquota = 0.075
elif salario <= 3751.05:
    aliquota = 0.15
elif salario <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275
desconto = aliquota * salario
salario = salario - desconto
print(f"Seu salário atualizado pós IR é R${salario }")


nome = input("Me fale seu nome:\n")
entrar = input("Você quer entrar na calculadora?s/n\n")
if entrar == 's':
    numero1 = float(input("Digite um número\n"))
    numero2 = float(input("Digite um número\n"))
    operacao = input("Qual operação você quer fazer?\nsoma\nsubtração\ndivisão\nmultiplicação\n")
    if operacao == 'soma':
        print(f"A soma entre {numero1} e {numero2} é {format(numero1 + numero2)}")
    elif operacao == 'sub':
        print(f"A subração entre {numero1} e {numero2} é {format(numero1 - numero2)}")
    elif operacao == 'div':
        print(f"A divisão entre {numero1} e {numero2} é {format(numero1 / numero2)}")
    else:
        print(f"A multiplicação entre {numero1} e {numero2} é {format(numero1 * numero2)}")
else:
    print(f'jaé{nome}.')
'''