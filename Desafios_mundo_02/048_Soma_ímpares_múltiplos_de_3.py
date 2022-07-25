print('***'*32); print('\n')

'''Faça um programa que calcule a soma entre todos os números que 
são múltiplos de 3 e que se encontram no intervalo de 1 até 500.'''

soma = 0 # acumulador
cont = 0 # contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('>> A Soma de {} números Ímpares de 1 a 500 é: {} <<'.format(cont, soma))

print('\n')
print('\033[31;1m***\033[m'*32)

