print('-=-'*35); print('\n')

''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''


velo = float(input('Velocidade do Carro em km/h: '))
if velo > 80:

    multa = (velo - 80) * 7
    print('\n>> vc foi MULTADO por EXCESSO de Velocidade <<\n'
          '>> Multa de R$7,00 por KM excedido <<.\n'
          '** Valor da Multa R${:.2f}'.format(multa))
else:
    print('\n** Velocidade Permirtida ! **')


