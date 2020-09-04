import math

num = float(input('Digite um Número: '))
print('O número \033[1;31m{}\033[m tem a parte inteira \033[1;34m{}'.format(num, math.floor(num)))
