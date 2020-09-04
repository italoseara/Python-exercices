termos = int(input('Quantos termos deve ter a sequencia? '))
t1 = 0
t2 = 1
cont = 0
if termos == 1:
    print('0 -> FIM')
else:
    print('0 -> 1 ->', end=' ')
    while termos - 2 != cont:
        cont += 1
        t3 = t2 + t1
        t2 = t3
        t1 = t2
        print('{} ->'.format(t3), end=' ')
    print('FIM')
