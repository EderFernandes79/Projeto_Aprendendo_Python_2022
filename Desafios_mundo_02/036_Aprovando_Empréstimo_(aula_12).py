



print('***'*30); print('\n')

'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
  A prestação mensal não pode exceder 30% do salário ou então o empréstimo 
  será negado.
'''

print('-==-'*7)
print ('FINANCIAMENTO IMOBILIÁRIO:')
print ('-==-'*7)

print('\n')

casa = float(input('Valor da Casa: R$ '))
sal = float(input('Salário Atual: R$ '))
anos = int(input('Pagar em quantos Anos?: '))

parcela = casa / (anos * 12)
minimo = sal * 0.30

print('\n')

if parcela >= minimo:
    print('>> Empréstimo NEGADO ! <<')
    print('>> Parcela de R$ {:.2f} maior que 30% do Salário de R$ {:.2f} <<'.format(parcela, sal))
else:
    print('** Empréstimo APROVADO:\n** Valor da Parcela R$ {:.2f}'.format(parcela))
    




print('\n')
print('***'*32)

