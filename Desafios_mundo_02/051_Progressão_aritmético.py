print('***'*32); print('\n')

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

print('=======================')
print('PROGRESSÃO ARITMÉTICA:')
print('======================='); print('\n')

primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('\n')

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c),end=' - ')
print('FIM')

print('\n')
print('***'*32)

