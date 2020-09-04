cont50 = cont20 = cont10 = cont1 = 0

print('='*30)

valor = int(input('Valor a ser sacado: R$'))

while valor >= 50:
    cont50 += 1
    valor -= 50

while valor >= 20:
    cont20 += 1
    valor -= 20

while valor >= 10:
    cont10 += 1
    valor -= 10

while valor >= 1:
    cont1 += 1
    valor -= 1

if cont50 != 0:
    print(f'{cont50} Cédulas de R$50')
if cont20 != 0:
    print(f'{cont20} Cédulas de R$20')
if cont10 != 0:
    print(f'{cont10} Cédulas de R$10')
if cont1 != 0:
    print(f'{cont1} Cédulas de R$1')

print('='*30)
