lista = list()

while True:
    a = int(input('Digite um valor: '))
    if a in lista:
        print('Número Duplicado, não vou adicionar!')
    else:
        print('Número Adicionado com Sucesso!')
        lista.append(a)
    r = str(input('Deseja continuar? [s/n] ')).lower()
    if r == 'n':
        break
lista.sort()
print(f'Você digitou os números {lista}')