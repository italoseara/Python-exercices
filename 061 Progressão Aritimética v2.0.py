pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont != 10:
    cont += 1
    print('{} ->'.format(pt), end=' ')
    pt = pt + razao
print('FIM')
