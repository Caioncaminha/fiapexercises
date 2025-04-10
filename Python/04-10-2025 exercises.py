'''1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.'''

nota = input("Digite uma nota entre zero e dez:\n")
while not (nota.isnumeric() and 0 <= int(nota) and int(nota) <= 10):
    print("Valor inválido")
    nota = input("Digite uma nota entre zero e dez:\n")
nota = int(nota)
print(f"Sua nota é {nota}.")


'''2- Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''



'''
3- Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.'''

'''4- Faça um programa que leia 5 números e informe a soma e a média dos números.'''

'''5- Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.'''

'''6- Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.'''

'''7- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''

'''8- A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.'''

'''9- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números ímpares.'''

'''10 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120'''

'''11 - Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

'''12 - Faça um programa que calcule o mostre a média aritmética de N notas.'''

'''13 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que:
1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.'''

'''14 - Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.'''

'''15 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados
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