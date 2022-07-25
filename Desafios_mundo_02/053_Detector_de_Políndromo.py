print('***'*32); print('\n')

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
ANOTARAM A DATA DA MARATONA.'''

print('***********')
print('POLÍNDROMO')
print('***********'); print('\n')

frase = str(input('Digite uma Frase: ')).upper().strip(); print('\n')
palavras = frase.split()    #separa as palavras da frase para gerar lista
juntar = ''.join(palavras)  #junta as palavras eliminando espaços
inverso = juntar[::-1]      #inverter a frase / fatiamento
#inverso = ''               

'''
for letra in range(len(juntar) -1 , -1, -1):     #inverter a frase
    inverso += juntar[letra]
print('o Inverso de {} é: "{}"'.format(frase,inverso)) 
'''

print('o Inverso de {} é: "{}"'.format(frase,inverso))

if inverso == juntar:
    print('\n** A frase {} é um PALÍNDROMO ! **'.format(frase))
else:
    print('\n>> A frase NÃO é um PALÍNDROMO !! <<'.format(frase))

    

print('\n')
print('***'*32)
