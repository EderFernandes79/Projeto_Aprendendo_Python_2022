print('*--*'*40) ; print('\n')

''' Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 parta viagens mais longas.'''

dist = float(input('Distancia em km: ')) ; print('\n')

print('sua viagem será de {}km'.format(dist))

if dist <= 200:
    preco = dist * 0.50
    print('** R$0.50 por km até 200km**\n>> Custo da Passagem: R${:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('** R$0.45 a cima de 200km**\n>> Custo da Passagem: R${:.2f}'.format(preco))

print('\n')

