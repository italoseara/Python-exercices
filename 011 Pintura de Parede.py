lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de \033[1;31m{}\033[m x \033[1;31m{}\033[m e sua área é de \033[1;34m{:.1f}m²\033[m'.format(lp, ap, lp * ap))
print('Para pintar sua parede será necessário \033[1;34m{:.1f}L\033[m de tinta'.format((lp * ap) / 2))
