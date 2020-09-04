menor = 0
maior = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento de alguém: '))
    idade = 2019 - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Nesse grupo existem {} pessoas maiores de idade e {} menores de idade!'.format(maior,  menor))
