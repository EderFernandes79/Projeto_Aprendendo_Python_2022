print('***'*40)
print(' ')

''' Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção Inteira.'''


import math

n = float(input('digite um numero: '))

print('a posição inteira de {} é: {}'.format(n, math.trunc(n)))