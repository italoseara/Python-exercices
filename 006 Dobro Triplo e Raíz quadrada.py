n = int(input('Digite um número: '))
print('O dobro de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format(n, n * 2))
print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format(n, n * 3))
print('A raiz quadrada de \033[1;31m{}\033[m é \033[1;34m{:.2f}\033[m'.format(n, n ** 0.5))
