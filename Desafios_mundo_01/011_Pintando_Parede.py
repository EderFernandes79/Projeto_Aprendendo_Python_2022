print('@@@'*40)
print('\n')

'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados'''


print('Medidas da Parede\n')

l = float(input('largura: '))
a = float(input('altura: '))
t = (l*a)/2

print('\n>> area da parede: {:.2f}m²\n>> é preciso {:.2f}l de tinta'.format(l*a,t) )
