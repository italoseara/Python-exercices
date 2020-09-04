from random import randint
from time import sleep

mega_sena = list()
lista = list()
cont = cont2 = 0

print('-' * 30)
print('{:^30}'.format('MEGA SENA'))
print('-' * 30)

jogos = int(input('Quantos jogos quer que eu sorteie? '))

print(f'-=-=-=  SORTEANDO {jogos} JOGOS  -=-=-=\n')

while cont2 != jogos:

    cont = 0

    while cont != 6:
        sorteado = randint(1, 60)

        if sorteado not in mega_sena:
            mega_sena.append(sorteado)
            cont += 1
    
    mega_sena.sort()
    lista.append(mega_sena[:])
    mega_sena.clear()

    cont2 += 1

for x, y in enumerate(lista):
    sleep(1)
    print(f'Jogo {x + 1}: {y}')

print('\n-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=')