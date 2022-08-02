print('***'*32); print('\n')

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

print('==========')
print('FATORIAL')
print('=========='); print('\n')

num = int(input('Número do Fatorial: ')); print('\n')
cont = num
fat = 1


while cont > 0:
    
    print('{} '.format(cont), end=' ')

    if cont > 1:
        print('x', end=' ')
    else:
        print(':', end=' '); print('\n')
    
    fat *= cont
    cont -= 1
   
print('O fatorial de {}! é : {}'.format(num, fat))

print('\n'); print('***'*32)