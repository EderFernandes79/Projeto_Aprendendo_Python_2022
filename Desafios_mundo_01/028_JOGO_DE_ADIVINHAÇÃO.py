print('***'*40); print('\n')

''' Escreva um programa que faça o computador “pensar” em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''


import random
from time import sleep

maquina = random.randint(0,5)

print('-*-'*20)
print('JOGO DE ERRO E ACERTO')
print('-*-'*20)
print('\n')


jogador = int(input('Digite um nº de 0 a 5: '))

print('PROCESSANDO...')
sleep(2)
print('\n')

if jogador == maquina:
    print(' ** vc Venceu ! **')
else:
    print('>> vc Perdeu ! <<\n\n** o nº escolhido foi: {} **'.format(maquina))



print('\n\n')
print('***'*20)




