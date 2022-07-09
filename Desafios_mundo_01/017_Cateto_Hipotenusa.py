print('***'*40)
print(' ')

'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''


import math

cO = float(input('C.Oposto: '))
cA = float(input('C.Adjacente: '))

h = math.hypot(cO, cA)

#h = (cO**2 + cA**2) ** (1/2)

print('\no comprimento da Hipotenusa é: {:.2f}'.format(h))
