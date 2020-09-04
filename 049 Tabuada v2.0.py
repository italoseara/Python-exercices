num = int(input('Digite um número: '))
n = 0
print()
print('\033[1;31m-\033[m' * 15)
for c in range(1, 11):
    n += 1
    print('\033[1;30m{} x {} = {}\033[m'.format(num, n, num * n))
print('\033[1;31m-\033[m' * 15)
