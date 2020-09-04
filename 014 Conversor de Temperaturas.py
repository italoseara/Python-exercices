c = float(input('Informe a temperatura em °C: '))
f = c * 1.8 + 32
print('A temperatura de \033[1;31m{:.1f}°C\033[m corresponde a \033[1;34m{:.1f}°F\033[m!'.format(c, f))
