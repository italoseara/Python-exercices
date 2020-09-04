n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
print('\n\033[mO número {} foi divisível por {} números'.format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
