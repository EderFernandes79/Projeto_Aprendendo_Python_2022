print('***'*40); print('\n')

'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
e todas as informações possíveis sobre ele.'''


print('====* Curso em Video *====')
print(' ')

a = input('digite algo: ')
print('O tipo desse valor é: ',type(a))
print(' ')

print('só tem espaços?: ',a.isspace())
print('é alfanumérico?: ',a.isalnum())
print('é alfabético?: ',a.isalpha())
print('está em maiúsculo?: ',a.isupper())
print('está em minúsculo?: ',a.islower())
print('está em maiúscula e minúsculas?: ',a.istitle())
print('é um número?: ',a.isnumeric())
print('está em decimal?: ',a.isdecimal())
print('é identificador?: ',a.isidentifier())

print('é digito?: {}'. format(a.isdigit()))
print('é imprimível?: {}'.format(a.isprintable()))
print(a.isascii())



