jogador = dict()

jogador['nome'] = input('Nome do jogador: ')

jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))

gols = list()
for x in range(jogos):
    gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for x, y in enumerate(gols):
    print(f'   => Na Partida {x+1}, fez {y} gols.')
print(f'Foi um total de {jogador["total"]}')
