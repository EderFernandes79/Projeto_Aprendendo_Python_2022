print('***'*32); print('\n')

from time import sleep

'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

print('==============')
print('MENU DE OPÇÕES')
print('=============='); print('\n')

n1 = int(input('** 1º valor: '))
n2 = int(input('** 2º valor: '))
op = 0

while op != 5:
   
    print('''\nEscolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('\n>>> Sua opção: '))

    
    if op == 1:
        soma = n1 + n2
        print('\n**Soma entre: {} e {} é: {}'.format(n1, n2, soma))

    elif op == 2:
        mult = n1 * n2
        print('\n** A multiplicação entre: {} e {} é: {}'.format(n1, n2, mult))

    elif op == 3:
        if n1 > n2:
            maior = n1
            print('\n** O Maior valor entre {} e {} é: {}'.format(n1, n2, maior))
        else:
            maior = n2
            print('\n** O Maior valor entre {} e {} é: {}'.format(n1, n2, maior))

    elif op == 4:
        print('\nDigite outros valores: ')   
        n1 = int(input('\n** 1º valor: '))
        n2 = int(input('** 2º valor: '))

    elif op == 5:
        print('\n>> Ação Finalizada! <<')
    else:
        print('\n>> OPÇÃO INVÁLIDA, REPITA ! <<')

    print('\n')
    print('-=-=-='*6)
    sleep(2)
print('>>>>>>>>> FIM <<<<<<<<<<')
print('\n'); print('***'*32)
