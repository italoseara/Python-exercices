sexo = str(input('Gênero: (m para Masculino ou f para Feminino) ')).lower()
while sexo != 'm' and sexo != 'f':
    print()
    print('Gênero Desconhecido! digite m para Masculino ou f para Feminino!')
    print()
    sexo = str(input('Gênero: ')).lower()
print('Informação Válida!')