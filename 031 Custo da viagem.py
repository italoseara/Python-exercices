distancia = float(input('\033[1;33mDistância da viagem (km): \033[m'))
if distancia <= 200:
    print('\033[1;33mO preço da passagem será de R${:.2f}\033[m'.format(distancia * 0.50))
else:
    print('\033[1;33mO preço da passagem será de R${:.2f}\033[m'.format(distancia * 0.45))
