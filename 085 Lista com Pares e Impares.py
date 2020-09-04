lista = [[], []]

for x in range(0, 7):
    a = int(input(f'{x + 1}° valor: '))
    if a % 2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)

print('\033[1m-=\033[m' * 25)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')