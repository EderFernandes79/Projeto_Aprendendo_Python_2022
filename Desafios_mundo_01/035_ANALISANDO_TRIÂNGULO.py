print('***'*40); print('\n')

'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

print('-*-'*20)
print('Seguimentos em "cm" para formar ou não um Triangulo:')
print('---'*20) ; print(' ')

a = float(input('seg. 01: '))
b = float(input('seg. 02: '))
c = float(input('seg. 03: ')); print(' ')

if b+c>a and a+c>b and a+b>c:
    print('Forma um Triangulo')
else:
    print('Não forma Triangulo')
