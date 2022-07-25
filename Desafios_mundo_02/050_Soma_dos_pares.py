print('***'*32);print('\n')

''' Desenvolva um programa que leia 6 números inteiros e 
mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for ímpar, desconsidere-o.'''

print('+++'*8)
print('SOMANDO 6 NÚMEROS PARES')
print('+++'*8); print('\n')

soma = 0
cont = 0

for num in range(1, 7):
    num = int(input('{}º Número: '.format(num)))
    if num % 2 == 0:
        soma += num
        cont += 1     
print('\nA Soma dos {} Pares é: {}'.format(cont, soma))

print('')
print('\033[35;1m***\033m'*32)
print('FIM')