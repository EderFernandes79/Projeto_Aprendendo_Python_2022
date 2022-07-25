print('***'*32); print('\n')

print('============')
print('TABUADA 2.0')
print('============')

num = int(input('\nNúmero para Tabuada: ')); print('\n')

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))

print(' ')
print('\033[34;1m***\033[m'*32)