p = float(input('Qual o preço do produto? R$'))
d = (p * 5) / 100
print('Caso o produto tenha 5% de desconto, o seu valor passará a ser \033[1;32mR${:.2f}'.format(p - d))
