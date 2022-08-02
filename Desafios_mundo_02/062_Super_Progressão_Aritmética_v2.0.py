print('==='*32); print('\n')


'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
>> usando o while << .'''


print('==================================')
print('GERADOR DE PROGRESSÃO ARITMÉTICA:')
print('==================================='); print('\n')


termo1 = int(input('1º Termo: '))
razao = int(input('Razão: ')); print('\n')
termo = termo1
cont = 1

while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    cont += 1
print('** Fim ** ')

print('\n'); print('==='*32)