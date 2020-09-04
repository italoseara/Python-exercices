sexo = a = b = c = continuar = 0
while True:
    print('\033[1m-' * 25)
    print('{:^21}'.format('CADASTRE UMA PESSOA'))
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        a += 1
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Sexo [M/F]: ')).lower()
    if sexo == 'm':
        b += 1
    elif sexo == 'f' and idade <= 20:
        c += 1
    print('-' * 25)
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar? [S/N]')).lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        sexo = continuar = 0
print()
print(f'{a} Pessoas tem Mais de 18 anos')
print(f'{b} Homens foram cadastrados')
print(f'{c} Mulheres têm menos de 20 anos')