from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = {}

print('Valores Sorteados:')
for x in range(4):
    jogada = randint(1, 6)
    jogadores[f'jogador{x + 1}'] = jogada
    print(f'Jogador {x+1} tirou: {jogada}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos jogadores:')
for x, y in enumerate(ranking):
    print(f'{x+1}° Lugar: {y[0]} com {y[1]}')
    sleep(1)