numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',\
          'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

while True:
    num = int(input('Digite um Número entre 0 e 20: '))

    if num > 20 or num < 0:
        print('Tente Novamente!', end=' ')

    else:
        break

print(f'O número digitado foi o número {numeros[num]}')