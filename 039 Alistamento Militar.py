ano = int(input('Ano de nascimento: '))
idade = 2019 - ano
if idade < 18:
    print('Faltam {} anos para você se alistar no exército!'.format(18 - idade))
elif idade > 18:
    print('Já passaram {} anos desde o dia do seu alistamento!'.format(idade - 18))
else:
    print('Já está na hora de você se alistar!')