print('{:=^51}'.format(' Calculadora de Fatorial '))
print()
n = int(input('Fatorial de: '))
fat = 1
print('{}! ='.format(n), end=' ')
for c in range(n, 0, -1):
    print(c, end=' ')
    if c != 1:
        print('.', end=' ')
    else:
        print('=', end=' ')
    fat = fat * c
print(fat)
