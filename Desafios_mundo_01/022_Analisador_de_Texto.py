print('***'*40); print('')

''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''



n = str(input('nome: ')).strip() #elimina o espaço direto na string

print('>> maiusculas: {}'.format(n.upper()))
print('>> minusculos: ',n.lower())
print('>> qtde de letras no nome, sem espaços: ',len(n)-n.count(' '))
print('>> qtde de letra no 1º nome: ',n.find(' '))
