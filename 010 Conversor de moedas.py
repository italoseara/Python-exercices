r = float(input('Quanto dinheiro você tem na carteira? R$'))
print()
print('Com \033[1;32mR${:.2f}\033[m você pode comprar \033[1;32mUS${:.2f}\033[m'.format(r, r / 3.89))
