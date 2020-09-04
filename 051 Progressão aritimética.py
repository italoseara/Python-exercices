print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ut = pt + (10 - 1) * razao
for c in range(pt, ut + razao, razao):
    print(c, end=' -> ')
print('ACABOU')
