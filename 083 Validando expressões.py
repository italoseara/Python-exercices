lista = []
pa = pf = 0
ex = str(input('Digite uma expressão: '))
for c in range(0, len(ex)):
    lista.append(ex[c:c + 1])
for i, v in enumerate(lista):
    if v == '(':
        pa += 1
    elif v == ')':
        pf += 1
if pa == pf:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida')