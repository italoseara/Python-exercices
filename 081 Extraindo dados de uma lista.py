lista = []
cont = 0

while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    r = str(input('Deseja continuar? [s/n] ')).lower()
    if r == 'n':
        break
print(f'Você digitou {cont} números')
lista.sort(reverse=True)
print(f'Os valores em órdem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 Não faz parte da lista!')