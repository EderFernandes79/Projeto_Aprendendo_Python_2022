print('\033[31;1m***\033[m'*36); print('\n')

from random import randint
from time import sleep

''' Crie um programa que faça o computador jogar Jokenpô com você.'''

print('-=-'*6)
print('\033[35;1mJÔ...\033[33;1mKEN...\033[m\033[36;1mPÔ !!\033[m')
print('-=-'*6); print('\n')


itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)

print('''Sua Opção: 
[1] - pedra
[2] - papel
[3] - tesoura''')
jogador = int(input('Sua Jogada: ')); print('\n')

print('\033[35;1mJO...\033[m'); sleep(1)
print('\033[33;1mKEN...\033[m'); sleep(1)
print('\033[36;1mPÔ !!\033[m'); sleep(1)
print(' ')

print('==='*10)

if pc == 0: #pedra
    if jogador == 0:
        print('>> EMPATOU !! <<')
    elif jogador == 1:
        print('** VC VENCEU !! **')
    elif jogador == 2:
        print('>> VC PERDEU !! <<')
    else:
        print('## Jogada Inválida !! ##')

elif pc == 1: #papel
    if jogador == 0:
        print('** VC PERDEU !! **')
    elif jogador == 1:
        print('>> EMPATOU !! <<')
    elif jogador == 2:
        print('** VC VENCEU !! **')
    else:
        print('## Jogada Inválida !! ##')

elif pc == 2: #tesoura
    if jogador == 0:
        print('** VC VENCEU !! **')
    elif jogador == 1:
        print('>> VC PERDEU !! <<')
    elif jogador == 2:
        print('>> EMPATOU !! <<')
    else:
        print('## Jogada Inválida !! ##')

print('==='*10)

print('\n')
print('-=-'*10)
print('>> Computador: {} <<'.format(itens[pc]))
print('** Sua Jogada foi: {} **'.format(itens[jogador]))
print('-=-'*10)


print('\n')
print('\n')
print('\033[31;1m***\033[m'*36)
