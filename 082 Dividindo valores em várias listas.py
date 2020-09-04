lista = []
par = []
impar = []

while True:
    a = int(input('Digite um número: '))
    lista.append(a)
    r = str(input('Deseja continuar? [s/n] ')).lower()
    if r == 'n':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Lista completa: {lista}')
print(f'Lista de números pares: {par}')
print(f'Lista de números impares: {impar}')
