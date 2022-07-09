print('###'*40)
print('\n')

'''Escreva um programa que converta uma temperatura digitando 
em graus Celsius e converta para graus Fahrenheit.'''


t = float(input('temperatura ºC: '))
f = 9 * t / 5 + 32
print('temperatura de {:.2f}ºC é {:.2f} em ºF'.format(t,f))