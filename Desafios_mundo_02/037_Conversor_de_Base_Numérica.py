print('***'*32); print(' ')

'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


print('-#-'*9)
print('CONVERSOR DE BASE DECIMAL')
print('-#-'*9); print('\n')

num = int(input('>> Digite um Nº inteiro Qualquer: '))
print('\n')

print('''Escolha a Base de Conversão:
[1]-Binário
[2]-Octal
[3]-Hexadecimal''')
op = int(input('Opção: '))

print('\n')

if op == 1:
    print('O BINÁRIO de {} é: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O OCTAL de {} é: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O HEXADECIMAL de {} é: {}'.format(num, hex(num)[2:]))
else:
    print('>> Opção Não Existe, tente novamente !! <<')

print('\n')
print('***'*32)
