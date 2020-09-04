from math import sin, cos, tan, radians

angulo = int(input('Digite o ângulo que você deseja: '))
r = radians(angulo)
print('O Seno de \033[1;31m{}°\033[m é \033[1;34m{:.2f}\033[m'.format(angulo, sin(r)))
print('O Cosseno de \033[1;31m{}°\033[m é \033[1;34m{:.2f}\033[m'.format(angulo, cos(r)))
print('E a Tangente de \033[1;31m{}°\033[m é \033[1;34m{:.2f}\033[m'.format(angulo, tan(r)))
