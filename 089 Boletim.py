boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])

    r = str(input('Quer continuar? [S/N] ')).lower()

    if r == 'n':
        break

print('-=' * 30)
print(f'N°. Nome      Média')
print('-' * 25)

for x, y in enumerate(boletim):
    print(f'{x:<4} {y[0]:<10} {y[2]:>8.1f}')
print('-=' * 30)

while True:
    r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r == 999:
        break
    else:
        print(f'Notas de {boletim[r][0]} são {boletim[r][1]}')
