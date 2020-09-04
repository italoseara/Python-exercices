n = int(input('Digite um número: '))
print()
if n % 2 == 0:
    print('\033[1;31m{}\033[m é \033[1;34mPar\033[m'.format(n))
else:
    print('\033[1;31m{}\033[m é \033[1;34mPar\033[m'.format(n))
