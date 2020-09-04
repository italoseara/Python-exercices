num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

cont9 = 0

for x in range(len(num)):
    if 9 == num[x]:
        cont9 += 1

print(f'Você digitou os valores {num}')

print(f'O número 9 foi digitado {cont9} vezes')

if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado nenhum vez')

print('Os números pares digitados foram: ', end='')
for x, y in enumerate(num):
    if y % 2 == 0:
        print(y, end=' ')