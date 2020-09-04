print('{:=^51}'.format(' Calculadora de Fatorial '))
print()
n = int(input('Fatorial de: '))
print()
x = n
z = n
fat = 1
y = 0
print('{}! ='.format(x), end=' ')
while y < n:
    print(z, end=' ')
    y = y + 1
    fat = fat * y
    if z != 1:
        print('.', end=' ')
    else:
        print('=', end=' ')
    z = z - 1
print('{}'.format(fat))
