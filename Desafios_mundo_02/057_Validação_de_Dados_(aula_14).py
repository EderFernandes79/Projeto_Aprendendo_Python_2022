print('***'*32); print('\n')

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 
M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''



sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()

while sexo not in 'FmMm':
    sexo = str(input('Opção Inválida, tente novamente!')).upper()[0].strip()
print('cadastro realizado com sucesso !')


print('\n'); print('***'*32)