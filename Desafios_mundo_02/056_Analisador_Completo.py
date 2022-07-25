from cgi import print_environ


print('==='*32); print('\n')

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

print('============')
print('ANALISADOR')
print('============'); print('\n')

soma = 0
media = 0
NomeHvelho = ''
maiorIddh = 0
qtdMulher20 = 0


for pessoa in range(1, 5):
    print('\n==={}ª Pesssoa: ==='.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idd = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip(); print('\n')
    soma += idd

    if pessoa == 1 and sexo in 'Mm' :
        maiorIddh = idd
        NomeHvelho = nome
    if sexo in 'Mm' and idd > maiorIddh :
        maiorIddh = idd
        NomeHvelho = nome
    if sexo in 'Ff' and idd < 20 :
        qtdMulher20 += 1

media = soma / 4

print('***'*20)
print('\n>> Média de Idade do grupo: {:.2f}'.format(media))
print('>> Nome do Homem mais Velho: {}'.format(NomeHvelho))
print('>> Idade do Homem mais Velho: {}'.format(maiorIddh))
print('\n** Mulheres com Menos de 20 anos: {}'.format(qtdMulher20)); print('\n')
print('***'*20)

print('\n'); print('==='*32)
