s = float(input('Salário atual: R$'))
if s <= 1250:
    a = ((s * 15) / 100) + s
    print('O salário de \033[1;32mR${:.2f}\033[m com um aumento de 15% será de: \033[1;32mR${:.2f}\033[m'.format(s, a))
else:
    a = ((s * 10) / 100) + s
    print('O salário de \033[1;32mR${:.2f}\033[m com um aumento de 10% será de: \033[1;32mR${:.2f}\033[m'.format(s, a))
