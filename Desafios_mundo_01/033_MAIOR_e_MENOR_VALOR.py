print('***'*40); print('\n')

''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = float(input('1º valor: '))
b = float(input('2º valor: '))
c = float(input('3º valor: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('Maior valor: {:.2f}'.format(maior))
print('Menor valor: {:.2f}'.format(menor))

