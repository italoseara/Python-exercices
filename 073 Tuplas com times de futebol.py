times = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'Internacional', 'Bahia', 'São Paulo', 'Grêmio',
         'Athletico-PR', 'Atlético', 'Goiás', 'Botafogo', 'Vasco', 'Fortaleza', 'Ceará SC', 'Fluminense',
         'Cruzeiro', 'CSA', 'Avaí', 'Chapecoense')

print('-=' * 60)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 60)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 60)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-=' * 60)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 60)
for x in range(len(times)):
    if 'Chapecoense' in times:
        chapeco = x + 1
print(f'Chapecoense está na {chapeco}° posição')
