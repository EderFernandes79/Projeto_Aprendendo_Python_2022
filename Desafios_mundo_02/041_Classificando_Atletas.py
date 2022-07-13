
from datetime import date


print('***'*34); print('\n')

'''A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

'''==================================================================================='''

print('=========================')
print('CLASSIFICAÇÃO DE ATLETAS:')
print('=========================')
print('\n')

anoNasc = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idd = anoAtual - anoNasc
cat = idd
print('\n')

print('**Sua Idade é {} anos:\n\n>>Sua Categoria: '.format(idd), end='')


if idd <= 9:
    print('MIRIM')
elif idd <= 14:
    print('INFANTIL')
elif idd <= 19:
    print('JÚNIOR')
elif idd <= 25:
    print('SÊNIOR')
else:
    print('MASTER')


print('\n')
