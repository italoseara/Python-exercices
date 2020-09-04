ano = int(input('Ano de nascimento: '))
idade = 2019 - ano
print('O Atleta tem {} Anos'.format(idade))
print('Classificação:')
if idade <= 9:
    print('\033[1;34mMIRIM\033[m')
elif 9 < idade <= 14:
    print('\033[1;34mINFANTIL\033[m')
elif 14 < idade <= 19:
    print('\033[1;34mJUNIOR\033[m')
elif 19 < idade <= 20:
    print('\033[1;34mSÊNIOR\033[m')
else:
    print('\033[1;34mMASTER\033[m')
