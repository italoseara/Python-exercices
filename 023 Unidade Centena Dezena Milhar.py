n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número \033[1;34m{}\033[m'.format(n))
print('Unidade: \033[1;34m{}\033[m'.format(u))
print('Dezena: \033[1;34m{}\033[m'.format(d))
print('Centena: \033[1;34m{}\033[m'.format(c))
print('Milhar: \033[1;34m{}\033[m'.format(m))
