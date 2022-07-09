print('+++'*40); print(' ')

''' Crie um programa que leia o nome de uma cidade diga se ela começa ou não
com o nome “SANTO”.'''


cid = str(input('** cidade: ')).upper().strip()

print('>> o nome começa com "SANTO"?: {}'.format('SANTO'in cid))
