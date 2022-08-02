print('***'*32); print('\n')

'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
os N primeiros elementos de uma Sequência de Fibonacci.

Exemplo:   0 – 1 – 1 – 2 – 3 – 5 – 8
          t1 + t2 + t3 '''

print('====================')
print('SEQUENCIA FIBONACCI')
print('====================');print('\n')

n = int(input('Quantidade de termos a ser mostrado: ')); print('\n')
t1 = 0
t2 = 1
cont = 3

print('{} + {} '.format(t1,t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' + {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
    
print(' == FIM')
print('\n'); print('***'*32)
