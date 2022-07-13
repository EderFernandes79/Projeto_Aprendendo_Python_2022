
print('***'*32); print('\n')

'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

print('------------------------')
print('GERENCIADOR DE PAGAMENTO')
print('------------------------'); print('\n')

valor = float(input('Valor Total da Compra: ')); print(' ')

print('>> FORMAS DE PAGAMENTO: '); print(' ')

print('''[1] - à vista Dinheiro/Cheque : 10% desc.
[2] - à vista no Cartão : 5% desc.
[3] - 2x no Cartão: sem desc.
[4] - 3x ou mais no Cartão: 20% de juros'''); print(' ')
opc = int(input('>>\033[34;1m Opção de Pagamento: \033[m')); print('\n')

print('** Valor da compra: R$ {:.2f}'.format(valor))

if opc == 1:
    total = valor - (valor * 0.10)
    print('>> Total com 10% de desconto: R$ {:.2f}'.format(total))  
elif opc == 2:
    total = valor - (valor * 0.05)
    print('>> Total com 5% de desconto: R$ {:.2f}'.format(total))
elif opc == 3:
    parcela = valor / 2
    print('>> Compra parcelada em 2x de R$ {:.2f} no cartão sem desconto e sem juros!'.format(parcela))
elif opc == 4:
    total = valor + (valor * 0.20) 
    numParc = int(input('Número de Parcelas: '))
    valorParc = total / numParc 
    print('\n')
    print('>> Total Parcelado em {}x de R$ {:.2f} no cartão com acréscimo de 20%: R$ {:.2f}'.format(numParc,valorParc,total))
else:
    print('\033[0;30;41m** OPÇÃO DE PARCELAMENTO INVÁLIDA, TENTE NOVAMENTE ! **\033[m')

print('\n'); print('***'*32)