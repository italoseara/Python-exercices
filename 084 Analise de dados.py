mais_leves = list()
mais_pesados = list()
todos = list()

pesado = leve = 0

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))

    if len(todos) == 0:
        leve = pesado = peso

    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso

    todos.append([nome.title(), peso])
    r = str(input('Deseja continuar? [S/N] ')).lower()
    if r == 'n':
        break

for x in range(0, len(todos)):
    if todos[x][1] == pesado:
        mais_pesados.append(todos[x][0])

for x in range(0, len(todos)):
    if todos[x][1] == leve:
        mais_leves.append(todos[x][0])

print(f'Um total de {len(todos)} pessoas foram cadastradas.')
print(f'O maior peso foi de {pesado}Kg. Peso de', end=' ')

for x in range(0, len(mais_pesados)):
    if x == len(mais_pesados) - 1:
        print(mais_pesados[x])
    else:
        print(f'{mais_pesados[x]}', end=', ')
print(f'O menor peso foi de {leve}Kg. Peso de', end=' ')

for x in range(0, len(mais_leves)):
    if x == len(mais_leves) - 1:
        print(mais_leves[x])
    else:
        print(f'{mais_leves[x]}', end=', ')