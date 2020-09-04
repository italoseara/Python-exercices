pn = float(input('Preço do produto: '))
print()
print('''Formas De Pagamento:
[1] Dinheiro / Cheque
[2] Cartão''')
print()
pagamento = int(input('Sua Opção: '))
if pagamento != 1 and pagamento != 2:
    print('\033[1;31mSelecione uma Forma Válida de Pagamento\033[m')
elif pagamento == 2:
    parcelas = int(input('Em quantas parcelas você deseja? '))
    if parcelas >= 3:
        print('O valor final do produto será de: R${:.2f} (20% de juros)'.format(pn + ((pn * 20) / 100)))
    elif parcelas == 2:
        print('O valor final do produto será de: R${:.2f}'.format(pn))
    else:
        print('O valor final do produto será de: R${:.2f} (5% de desconto)'.format(pn - ((pn * 5) / 100)))
else:
    print('O valor final do produto será de: R${:.2f} (10% de desconto)'.format(pn - ((pn * 10) / 100)))