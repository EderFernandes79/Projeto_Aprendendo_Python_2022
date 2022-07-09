print('***'*40)
print(' ')

'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.'''



'''
import math

a = float(input('angulo de : '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
'''

from math import radians, cos, tan, sin

a = float(input('angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('\n>> seno de {}: {:.2f}\n>> cosseno de {}: {:.2f}\n>> tengente de {}: {:.2f}'.format(a,s,a,c,a,t))