from time import sleep

print('\033[31;1m***\033[m'*32); print('\n')

'''Faça um programa que mostre na tela uma contagem regressiva para o 
estouro de fogos de artifício, indo de 10 até 0, com uma pausa 
de 1 segundo entre eles.'''

print('=-'*10)
print('CONTAGEM REGRESSIVA')
print('=-'*10); print('\n')

for c in range(5, -1, -1):
    sleep(0.25)
    print(c)
    sleep(0.25)

print('\n')
print('\033[32;1mBOM...BOM...POW...!\033[m\n\033[34;1m\nFELIZ NATAL !!\033[m')

print('\n')
