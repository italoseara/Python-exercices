cont = total = cont2 = 0
while True:
    print()
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))

    while cont2 == 0:
        barato = nome
        baratocusto = valor

        cont2 += 1

    if valor < baratocusto:
        barato = nome
        baratocusto = valor

    if valor >= 1000:
        cont += 1

    total += valor

    r = str(input('Deseja continuar? [S/N] ')).lower()
    if r == 'n':
        break

print()
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{cont} Produtos custaram mais que R$1000.00')
print(f'O produto mais barato foi {barato.title()}')
