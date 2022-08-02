print('***'*32); print('\n')

'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. 
No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('TRATANDO VÁRIOS VALORES:')
print('-=-=-=-=-=-=-=-=-=-=-=-=-='); print('\n')

n = soma = cont = 0

n = int(input('Digite um número ou [999] para Finalizar: '))

while n != 999:
    if n != 0 : 
        cont += 1
        soma += n 
        n = int(input('Digite um número ou [999] para Finalizar: '))

print('\nDigitados: {}\nSoma {} '.format(cont, soma))
 
print('\n ** FIM ** ')

print('\n'); print('***'*32)
