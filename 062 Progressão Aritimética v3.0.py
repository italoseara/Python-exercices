termos = 10
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
while termos != 0:
    cont = 0
    while cont != termos:
        cont += 1
        print('{} ->'.format(pt), end=' ')
        pt = pt + razao
    print('Pausa')
    termos = int(input('Deseja mostrar mais quantos termos? '))
print('FIM')
