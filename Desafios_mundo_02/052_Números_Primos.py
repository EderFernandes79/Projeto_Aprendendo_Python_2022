from json import tool
from traceback import format_exc
from turtle import end_fill


print('***'*32); print('\n')

'''Faça um programa que leia um número inteiro e diga 
se ele é ou não um número primo.
'''
print('=============')
print('NÚMERO PRIMO')
print('============='); print('\n')

num = int(input('Digite um número: ')); print('\n')
total = 0

for cont in range(1, num + 1):

    if num % cont == 0:
        total += 1

if total == 2 :
    print('>> número {} É PRIMO; pois '. format(num), end=' ')
else:
    print('** número {} NÃO É PRIMO, pois'.format(num), end=' ')
print('é divisivel {} vezes !'.format(total))





print('\n')
print('***'*32)

