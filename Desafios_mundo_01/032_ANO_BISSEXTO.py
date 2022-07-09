print('¨¨¨'*40); print('\n')

''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
    0 para ano atual.
'''

from datetime import date

print('Ano Comum ou Bissexto? ') ; print('\n')

ano = int(input('digite um ano ou 0 para ano atual: '))

if ano == 0:
    ano = date.today().year

if ano%4==0 and ano%100!=0 or ano%400==0:
    print('>> O Ano de {} é Bissexto ! <<'.format(ano))
else:
    print('** O Ano de {} é Comum !! **'.format(ano))

