print('***'*32); print('\n')
'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

print('*****************')
print('NÚMEROS COM FLAG')
print('*****************'); print('\n')

soma = cont = media = 0

while True:
    num = int(input('Entre com um número ou [999 para FIM]: '))
  
    if num == 999:
        break
    soma += num
    cont += 1
    media = cont / num

print(f'\n*** Quantidade de numeros digitados: {cont}')
print(f'>>> Soma dos numeros digitados: {soma}')
print(f'## Média dos digitados: {media}')

print('\n== FIM ==')
print('\n'); print('***'*32)