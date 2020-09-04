print('\033[1;33m-=-\033[m'*7)
print('\033[1;34m Calculadora de IMC\033[m')
print('\033[1;33m-=-\033[m'*7)
peso = float(input('Peso: '))
alt = float(input('Altura: '))
imc = peso / alt ** 2
print()
print('IMC: {:.2f}'.format(imc))
if imc <= 18.5:
    print('\033[1;31mAbaixo Do Peso!\033[m')
elif 18.5 < imc <= 25:
    print('\033[1;31mPeso Ideal!\033[m')
elif 25 < imc <= 30:
    print('\033[1;31mSobrepeso!\033[m')
elif 30 < imc <= 40:
    print('\033[1;31mObesidade!\033[m')
else:
    print('\033[1;31mObesidade Mórbida!\033[m')