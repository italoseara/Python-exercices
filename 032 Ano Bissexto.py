ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0:
    print('{} \033[1;31mé\033[m um ano bissexto!'.format(ano))
else:
    print('{} \033[1;31mnão é\033[m um ano bissexto!'.format(ano))
