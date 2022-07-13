
print('***'*32); print(' ')

''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

print('=======================')
print('MEDIDOR DE IMC CORPORAL')
print('=======================')
print('\n')

peso = float(input('Digite seu Peso: '))
alt = float(input('Dgite sua Altura: '))
imc = peso / (alt ** 2)
print('\n')

print('>> Seu IMC é: {:.2f}\n\n** Você está em: '.format(imc), end=' ')

if imc < 18.5:
    print('Abaixo do Peso Normal !!')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal !!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso !!')
elif imc >= 30 and imc < 40:
    print('Obesidade !!')
else:
    print('OBESIDADE MÓBIDA, SE CUIDE !!')

print('\n')
print('==='*32)

    
