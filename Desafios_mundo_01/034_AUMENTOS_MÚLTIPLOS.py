print('***'*40) ; print('\n')

'''Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''


sal = float(input('-- Salário R$ '))

if sal >= 1250:
    aum = (sal*0.10) + sal
    print('>> Salário de R$ {:.2f}\n** Novo Salário com 10% de aumento: R$ {:.2f}'.format(sal, aum))
else:
    aum = (sal*0.15) + sal
    print('>> Salário R$ {}\n** Novo Salário com 15% de aumento: R$ {}'.format(sal, aum))
