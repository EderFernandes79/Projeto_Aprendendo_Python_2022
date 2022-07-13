
print('***'*32); print('\n')

'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

'''====================================================================================='''


print('¨¨¨'*10)
print('CALCULANDO A MÉDIA de 2 NOTAS:')
print('¨¨¨'*10)
print('\n')

n1 = float(input('Nota 01: '))
n2 = float(input('Nota 02: '))

m = (n1 + n2) / 2

print('\n')
print('A Média é: {}'.format(m))
print('\n')

if m < 5:
    print('Você está REPROVADO !')
elif m >= 5 and m < 6.9:
    print('Você está em RECUPERAÇAO !')
else:
    print('Você está APROVADO !')

print('\n')
print('***'*32)



