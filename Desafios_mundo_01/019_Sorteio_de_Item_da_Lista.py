print('###'*40) ; print(' ')

'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela 
o nome do escolhido.'''


'''
import random

a1 = str(input('Aluno 01: '))
a2 = str(input('Aluno 02: '))
a3 = str(input('Aluno 03: '))
a4 = str(input('Aluno 04: '))
l = [a1, a2, a3, a4]

esc = random.choice(l)
'''

from random import choice


a1 = str(input('Aluno 01: '))
a2 = str(input('Aluno 02: '))
a3 = str(input('Aluno 03: '))
a4 = str(input('Aluno 04: '))

lista = [a1, a2, a3, a4]
sorteado = choice(lista)


print('\nO escolhido(a) foi: ', sorteado)