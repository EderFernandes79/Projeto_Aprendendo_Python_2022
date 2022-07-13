from ctypes.wintypes import FLOAT


print('***'*32); print(' ')

''''Desenvolva um programa que leia o comprimento de 3 RETAS e diga ao usuário
se elas podem ou não formar um triângulo; mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

print('=====================')
print('ANALISANDO TRIÂNGULO:')
print('=====================')

print('\nVALORES PARA CADA SEGMENTO:')
a = float(input('\nSeg. 01: '))
b = float(input('Seg. 02: '))
c = float(input('Seg. 03: '))

print('\n')

if b + c > a and a + c > b and a + b > c:
    print('Segmentos Formam um Triângulo: ', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELIS')
else:
        print('>> Não Formam um Triângulo: !! <<') 

print('\n')

