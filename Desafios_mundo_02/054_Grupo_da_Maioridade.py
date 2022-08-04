print('***'*32); print('\n')

''' Crie um programa que leia o ano de nascimento de 7 pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e
 quantas já são maiores.'''



from datetime import date

print('==================')
print('GRUPO, MAIORIDADE')
print('=================='); print('\n')

anoAtual = date.today().year
maior = 0
menor = 0

for cont in range(1, 8):
    anoNasc = int(input('>> Nascimento da {}ª pessoa: '.format(cont)))
    idd = anoAtual - anoNasc
    if idd >= 21:
        maior += 1
    else:
        menor += 1
print('\n>> Total de Maior idade: {}'.format(maior))
print('>> Total de Menor idade: {}'.format(menor))

print('')
print('***'*32)
