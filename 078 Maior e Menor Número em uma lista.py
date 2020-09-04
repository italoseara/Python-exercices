v = list()

for c in range(0, 5):
    v.append(int(input(f'Digite um número para a posição {c}: ')))
a = v[:]
a.sort()
print(f'Você Digitou os números {v}')
print(f'O menor valor digitado foi {a[0]} nas poições', end=' ')
for x in range(0, 5):
    if v[x] == a[0]:
        print(f'{x}...', end=' ')
print()
print(f'O maior valor digitado foi {a[4]} nas posições', end=' ')
for x in range(0, 5):
    if v[x] == a[4]:
        print(f'{x}...', end=' ')
