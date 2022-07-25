print('==='*32); print('\n')

''' Faça um programa que leia o peso de 5 pessoas. No final, 
mostre qual foi o maior e o menor peso lidos.'''

print('====================')
print('MAIOR E MENOR PESOS')
print('====================='); print('\n')


maior = 0
menor = 0

for pessoa in range(1, 6 ):
    peso = float(input('Peso {}ª pessoa: '.format(pessoa)))
    if pessoa == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\n>> Maior valor: {}kg\n>> Menor valor: {}kg'.format(maior, menor))

print('\n')
print('==='*32)
