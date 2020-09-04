n = 0
m = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para]: '))
    cont += 1
    m = m + n
print('Você digitou {} números!'.format(cont - 1))
print('A soma entre todos eles foi de: {}!'.format(m - 999))
