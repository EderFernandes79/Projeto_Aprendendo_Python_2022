print('""""'*40)
print('\n')

'''Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto.'''


prod = float(input('Preço: R$ '))

# p = p-(p*5/100)

print('valor com desconto de 5%:\nR$ {:.2f}'.format(prod-(prod * 5 / 100)))