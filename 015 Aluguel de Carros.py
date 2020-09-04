dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
preco = (dias * 60) + (km * 0.15)
print('O total a pagar é de \033[1;32mR${:.2f}'.format(preco))
