print('***'*40); print(' ')

'''Faça um programa que leia uma frase pelo teclado e mostre quantas 
vezes aparece a letra “A”, em que posição ela aparece a primeira vez 
e em que posição ela aparece a última vez.'''

f = str(input('frase: ')).upper().strip()

print('\n>> qtas vez aparece "A"? : {} vezes'.format(f.count('A')))
print('>> 1ª letra "A": {} posição'.format(f.find('A')+1))
print('>> ultima letra "A": {} posição'.format(f.rfind('A')+1))