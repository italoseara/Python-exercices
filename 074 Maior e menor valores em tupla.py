from random import randint

cont = menor = maior = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os números sorteados foram', end=' ')

for x, y in enumerate(tupla):
    if x == 0:
        menor = maior = y

    print(y, end=' ')

    if y > maior:
        maior = y

    if y < menor:
        menor = y

print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')