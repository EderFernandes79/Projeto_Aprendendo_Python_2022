print('***'*32); print('\n')

''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

print('-=-'*6)
print('COMPARANDO dois NÚMEROS')
print('-=-'*6); print('\n')

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

print('\n')

if n1 > n2:
    print('O 1º valor é MAIOR' )
elif n2 > n1:
    print('O 2º valor é MAIOR')
else:
    print('>> NÃO existe valor MAIOR, os dois são IGAUIS !! <<')

print('\n')





