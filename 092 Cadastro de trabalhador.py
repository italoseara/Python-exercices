trabalhador = {
    'nome': input('Nome: '),
    'idade': 2020 - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de trabalho (0 nao tem): '))
    }

if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratacao: '))
    trabalhador['salario'] = float(input('Salario: R$'))
    trabalhador['aposentadoria'] = (35 - (2020 - trabalhador['contratacao'])) + trabalhador['idade']

print()

for x, y in enumerate(trabalhador):
    print(f' - {y} tem o valor {trabalhador[str(y)]}')