matriz = [[], [], []]
soma = soma2 = maior = 0

for x in range(0, 3):
    for y in range(0, 3):
        a = int(input(f'Digite um valor para [{x}, {y}]: '))

        if a % 2 == 0:
            soma += a
        
        if y == 2:
            soma2 += a
        
        if x == 1 and a > maior:
            maior = a

        matriz[x].append(a)

print('-=' * 30)

print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')

print('-=' * 30)

print(f'A soma de todos os números pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma2}')
print(f'O maior valor da segunda linha é: {maior}')