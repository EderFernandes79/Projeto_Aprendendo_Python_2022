print('***'*32); print('\n')

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

print('=======================')
print('MAIOR E MENOR VALORES')
print('======================='); print('\n')


num = media = soma = maior = menor = cont = 0
resp = 's'


while resp in 'Ss':
    num = int(input('\n>> Um número: '))
    resp = str(input('\n** Continuar ? [S/N]: ')).upper().strip()[0]
    print('==='*8)


    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / cont

print('\n>> media: {}'.format(media))
print('** maior: {}\n** menor: {}'.format(maior, menor))

print('\n*** FIM ***')
print(''); print('***'*32)
