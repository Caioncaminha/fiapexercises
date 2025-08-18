'''1. Número Positivo:
Solicite um numero ao usuario e, se ele for maior que 0, exiba "Numero
positivo!".
'''
def positivo():
    num = input("Digite um número positivo: \n")
    num = int(num)
    if num > 0:
        print("Número positivo!")
    else:
        print("Um número POSITIVO!")
        num = input("Digite um número positivo: \n")

'''
2. Número Par:
Peca ao usuario um numero e, se o resto da divisao por 2 for 0, exiba
"Numero par!".
'''
def resto2():
    num = input("Digite um número divisível por 2: \n")
    num = int(num)
    if num%2 == 0:
        print("Número par")
    else:
        print("Um número divisível por 2.")
        num = input("Digite um número divisível por 2: \n")

'''
3. Contém a Letra 'a':
Solicite uma palavra e, se ela contiver a letra "a" (maiuscula ou minuscula),
exiba "Contem a letra a!".
'''
def palavraLetraA():
    palavra = input("Digite uma palavra que contenha a letra 'A': \n")
    if "a" in palavra.lower:
        print("Contém a letra 'a'")
    else:
        print("A palavra não contem a letra 'a'")
        palavra = input("Digite uma palavra que contenha a letra 'A': \n")

'''
4. Temperatura Alta:
Peca a temperatura e, se ela for maior que 30°C, exiba "Esta quente!".
'''
def tempAlta():
    temp = input("Escreva a temperatura atual: \n")
    temp = int(temp)
    if temp >= 30:
        print("Está quente.")
    else:
        print("Não está quente.")

'''
5. Número Igual a 10:
Solicite um numero e, se ele for igual a 10, exiba "Numero e 10!".
'''
def igual10():
    num = input("Escreva o número 10: \n")
    num = int(num)
    if num == 10:
        print("Você escreveu o número 10.")
    else:
        print("Escreva o número 10.")

'''
6. Par ou Ímpar:
Solicite um numero inteiro. Se o numero for par, exiba "Par"; caso
contrario, exiba "Impar".
'''
def parImpar():
    num = input("Escreva um número inteiro")
    num = int(num)
    if num%2 == 0:
        print("O número escrito é par.")
    else:
        print("O número escrito é ímpar.")

'''
7. Validação de Senha:
Peca uma senha ao usuario e compare com uma senha pre-definida (por
exemplo, "seguro123"). Se for igual, exiba "Acesso concedido!"; senao,
"Acesso negado!".
'''
def senha():
    senha = "seguro123"
    pedido = input("Escreva a senha. \n")
    if pedido == senha:
        print("Acesso concedido!")
    else:
        print("Acesso negado.")

'''
8. Maior ou Menor de Idade:
Solicite o ano de nascimento do usuario. Se o usuario tiver 18 anos ou
mais, exiba "Maior de idade"; caso contrario, "Menor de idade".
'''
def maiorIdade():
    nasci = input("Digite o seu ano de nascimento: \n")
    if 2025 - nasci >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")

'''
9. Número Negativo ou Não:
Peca um numero e, se ele for negativo, exiba "Numero negativo"; senao,
exiba "Numero nao e negativo".
'''
def negativo():
    num = input("Digite um número.")
    num = int(num)
    if num < 0:
        print("Número negativo")
    else:
        print("Número não é negativo.")

'''
10. Texto Vazio ou Não:
Solicite ao usuario que digite um texto. Se o usuario nao digitar nada, exiba
"Nenhum texto digitado"; caso contrario, "Texto recebido".
'''
def vazio():
    texto = input("Digite algo. \n")
    if texto.strip == "":
        print("Nenhum texto digitado.")
    else:
        print(f"Você digitou {texto}")

'''
11. Classificação de Notas:
Peca a nota do aluno e classifique:
o Nota ≥ 90: "Conceito A"
o Nota ≥ 80: "Conceito B"
o Nota ≥ 70: "Conceito C"
o Abaixo de 70: "Conceito D"
'''
def notas():
    nota = input("Digite sua nota: \n")
    if nota >= 90:
        print("Coinceito A")
    elif nota >= 80 and nota < 90:
        print("Conceito B")
    elif nota >= 70 and nota < 80:
        print("Coinceito C")
    else:
        print("Conceito D")

'''
12. Faixa de Temperatura:
Solicite a temperatura:
o Acima de 30°C: "Muito quente"
o Entre 15°C e 30°C: "Temperatura agradavel"
o Abaixo de 15°C: "Frio"
13. Desempenho do Aluno:
Solicite uma pontuacao (0 a 100):
o Pontuacao ≥ 85: "Excelente"
o Entre 70 e 84: "Bom"
o Entre 50 e 69: "Regular"
o Abaixo de 50: "Insuficiente"
14. Clima do Dia:
Peca ao usuario para informar o tempo (ex.: "ensolarado", "nublado",
"chuvoso") e exiba uma mensagem especifica para cada caso usando elif.
(Exemplo: se "ensolarado", exiba "Dia perfeito para sair"; se "chuvoso",
"Leve um guarda-chuva"; senão, "Aproveite o dia!")
15. Classificação Etária:
Solicite a idade e classifique:
o Menor que 12: "Crianca"
o Entre 12 e 17: "Adolescente"
o Entre 18 e 64: "Adulto"
o 65 ou mais: "Idoso"
16. Número no Intervalo (10 a 20):
Solicite um numero e, se ele estiver entre 10 e 20 (inclusive), exiba
"Numero no intervalo".
17. Número Positivo e Par:
Peca um numero e, se ele for positivo e par, exiba "Numero positivo e par".
18. Acesso com Documento:
Solicite a idade e se o usuario possui documento ("sim" ou "nao"). Se a
idade for maior ou igual a 18 e a resposta for "sim", exiba "Acesso
permitido".
19. Desconto para Idosos ou Clientes com Cartão:
Solicite a idade e se o cliente possui cartao de desconto ("sim" ou "nao").
Se a idade for 65 ou mais ou se o cliente tiver o cartao, exiba "Desconto
aplicado".
20. Autorização para Votar:
Solicite a idade e se o usuario possui impedimento para votar ("sim" ou
"nao"). Se a idade for maior ou igual a 16 e a resposta for "nao", exiba "Pode
votar".
21. Verificação de Caracteres na Senha:
Solicite uma senha e, se ela contiver pelo menos um dos caracteres "!",
"@" ou "#" e alem disso tiver mais de 10 caracteres exiba "Senha forte".
22. Número Dentro do Intervalo (1 a 100) com Not:
Solicite um numero e, se não for menor que 1 e nao for maior que 100,
exiba "Numero dentro do intervalo de 1 a 100". Utilize o operador not para
simplificar a condicao.
23. Aprovação do Aluno:
Solicite a nota e a frequencia (em porcentagem) do aluno. Se a nota for
maior ou igual a 6 e a frequencia for maior ou igual a 75, exiba "Aprovado".
24. Recuperação ou Reprovação:
Solicite a nota e a frequencia. Se a nota for menor que 6 e a frequencia for
maior ou igual a 75, exiba "Faca a recuperacao"; se a nota for menor que 6
e a frequencia for menor que 75, exiba "Reprovado". Se a nota for maior
que 6 e a frequencia maior que 75, exiba “Aprovado”.
25. Aposentadoria:
Solicite o ano de nascimento e o tempo de contribuicao. Condicoes para
aposentadoria:
• Se a idade for maior ou igual a 65
• Idade for maior ou igual a 60 e tempo de contribuicao for maior ou
igual a 30)
Exiba "Pode se aposentar" se uma dessas condicoes for satisfeita.
26. Acesso ao Sistema:
Solicite o login e a senha. Se o login for "admin" e a senha for "1234", exiba
"Acesso liberado"; senao, exiba "Acesso negado".
27. Ano Bissexto:
Solicite um ano e, se ele for divisivel por 4 e (nao divisivel por 100 ou
divisivel por 400), exiba "Ano bissexto".
(Utilize parênteses para deixar clara a precedência dos operadores.)
28. Promoção de Produto:
Solicite o preco do produto e se ele esta em estoque ("sim" ou "nao"). Se o
preco for menor que 50 e o produto estiver em estoque, exiba "Produto em
promocao".
29. Participação em Sorteio:
Solicite a idade e se o usuario ja participou de um sorteio ("sim" ou "nao").
Se a idade for maior ou igual a 18 e a resposta for "nao", exiba "Pode
participar do sorteio".
30. Bolsa de Estudos:
Solicite a media do aluno, a renda familiar e se participa de atividades
extracurriculares ("sim" ou "nao"). Condicoes para ser elegivel para bolsa:
• media for maior ou igual a 8 e renda for menor que 3000
• media for maior ou igual a 7 e participacao for "sim"
Se o aluno atende a qualquer um desses dois criterios, exiba "Elegivel para
a bolsa". Caso contrario exiba "Nao elegivel para bolsa"
'''
