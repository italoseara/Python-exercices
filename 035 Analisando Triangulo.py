print('\033[1;33m-=-\033[m'*10)
print('\033[1;34mAnalisador De Triângulos\033[m')
print('\033[1;33m-=-\033[m'*10)
a = int(input('Segmento 1: '))
b = int(input('Segmento 2: '))
c = int(input('Segmento 3: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Esses 3 Segmentos \033[1;32mPODEM FORMAR\033[m um Triângulo!')
else:
    print('Esses 3 Segmentos \033[1;31mNÃO PODEM FORMAR\033[m um Triângulo')
