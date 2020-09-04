cont = cont2 = velho = velhon = soma = 0
print('Digite os dados de 4 pessoas')
while cont != 4:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m, f]: '))
    soma += idade
    cont += 1
    if sexo == 'm':
        if idade > velho:
            velhon = nome
            velho = idade
    elif sexo == 'f':
        if idade <= 20:
            cont2 += 1
print(f'Media das idades: {soma / 4} anos')
print(f'O homem mais velho se chama {velhon}')
print(f'{cont2} mulheres são menores de 20 anos')
