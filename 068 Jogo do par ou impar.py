from random import randint

cont = 0
print('\033[1m-\033[m'*21)
print('Par ou impar')
print('\033[1m-\033[m'*21)
print()
while True:
    n = int(input('Diga um número: '))
    pi = str(input('Par ou impar? [P / I]: ')).lower()
    print()
    np = randint(0, 10)
    r = n + np
    print('\033[1m-\033[m'*61)
    print(f'Você jogou {n} e o computador jogou {np}. Total de {r} ', end='')
    if r % 2 == 0:
        print('Deu PAR')
    else:
        print('Deu ÍMPAR')
    print('\033[1m-\033[m'*61)
    print()
    if r % 2 == 0 and pi == 'p' or r % 2 != 0 and pi == 'i':
        print('\033[1m-\033[m'*61)
        print('Você VENCEU!')
        print()
        print('Vamos jogar Denovo!')
        print('\033[1m-\033[m'*61)
        print()
        cont += 1
    else:
        print(f'Você PERDEU! Ganhou um total de {cont} vez(es)')
        print()
        print('GAME OVER!')
        break
