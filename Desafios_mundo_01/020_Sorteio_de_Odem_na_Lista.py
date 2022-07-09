print('@@@'*40)
print(' ')

'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.'''


import random

a1 = str(input('al. 01: '))
a2 = str(input('al. 02: '))
a3 = str(input('al. 03: '))
a4 = str(input('al. 04: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('\nordem d4e apresentação: \n', lista)