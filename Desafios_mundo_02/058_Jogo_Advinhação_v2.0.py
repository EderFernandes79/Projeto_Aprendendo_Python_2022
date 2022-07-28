print('***'*32); print('\n')

''' Escreva um programa que faça o computador “pensar” em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer.
'''

print('-=-=-=-=-=-=-=-=-=-=')
print('JOGO DE ADVINHAÇÃO')
print('-=-=-=-=-=-=-=-=-=-='); print('\n')


import random
from time import sleep

pc = random.randint(0, 10)
print('** Pc escolhendo um número...')
sleep(0.25); print('\n')

acerto = False
tentativas = 0

while not acerto:
    jogador = int(input('\n>> Digite um número de 0 a 10: '))
    tentativas += 1
    
    if jogador == pc:
        acerto = True
    if jogador >= 11 :
        print('\nOpção Inválida, tente novamente!')
    else:
        if jogador < pc :
            print('Tá frio...mais...\n')
        elif jogador > pc :
            print('Tá quente...menos...\n')
   
print('\n** Vc Venceu com {} tentativas ***'.format(tentativas))
print('\n>> Escolha do Pc: {} <<'.format(pc))

print('\n'); print('***'*32)