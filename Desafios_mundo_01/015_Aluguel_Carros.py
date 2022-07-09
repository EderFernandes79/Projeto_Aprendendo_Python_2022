print('***'*40)
print('\n')

''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
    e a quantidade de dias pelos quais ele foi alugado. 
   *Calcule o preço a pagar, sabendo que
    o carro custa R$60 por dia e R$0,15 por Km rodado.'''


d = int(input('qtd de dias: '))
k = float(input('KM percorrido: '))

pg = d * 60 + k * 0.15

print('\n>>dias alugado: {}\n>>KM rodados: {}km\n>>A pagar: R$ {:.2f}'.format(d, k, pg))



