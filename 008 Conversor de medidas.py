met = float(input('Digite uma medida em metros: '))
print('A medida de \033[1;34m{}m\033[m corresponde a:'.format(met))
print('\033[1;34m{}km'.format(met / 1000))
print('{}hm'.format(met / 100))
print('{}dam'.format(met / 10))
print('{}dm'.format(met * 10))
print('{}cm'.format(met * 100))
print('{}mm'.format(met * 1000))
