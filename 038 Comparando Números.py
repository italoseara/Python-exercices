print('Digite Dois números inteiros')
print()
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
print()
if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}!'.format(n2, n1))
else:
    print('Os dois valores são iguais!')