from math import pow, sqrt

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('Hipotenuza: \033[1;34m{:.3f}\033[m'.format(h))
