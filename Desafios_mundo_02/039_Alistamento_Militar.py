
from xmlrpc.client import DateTime


print('+-+-'*25); print('\n')

'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

print('*-*-*'*4)
print('ALISTAMENTO MILITAR')
print('*-*-*'*4)
print('\n')

anoNasc = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idd = anoAtual - anoNasc
print('\n')

if idd < 18:
    falta = 18 - idd
    sera = anoAtual + falta
    print('*Idade: {} anos\n\n>> Ainda faltam {} para se alistar <<'.format(idd, falta))
    print('\n>> Seu Alistamento será em {} <<'.format(sera))

elif idd == 18 :
    print('*Idade: {} anos\n\n** PODE se Alistar!! ** '.format(idd))

elif idd > 18:
    falta = idd - 18
    foi = anoAtual - falta
    print('*Idade: {} anos\n\n** Já deveria ter se alistado há {} anos atrás!'.format(idd, falta))
    print('\n>> Seu Alistamento foi em {} <<'.format(foi))

print('\n')
print('---'*25)
print('\n')
