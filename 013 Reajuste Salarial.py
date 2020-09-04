s = float(input('Qual o salário do funcionário? R$'))
a = (s * 15) / 100
print('Caso o funcionário receba 15% de aumento, seu salário passará a ser \033[1;32mR${:.2f}'.format(s + a))
