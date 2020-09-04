from time import sleep
from random import randint

print('\033[1;33m-=-\033[m' * 20)
print('''\033[1;31mVamos brincar de Jo Ken Po?
Eu vou escolher Pedra, Papel ou Tesoura e você também!
Vamos ver quem é o melhor!''')  # Mensagem de inicio de jogo
print('\033[1;33m-=-\033[m' * 20)
print()
sleep(1)  # Aguarda 1s
input('\033[3;1mPress ENTER to Continue!\033[m')  # Uma pausa até o jogador pressionar ENTER
sleep(0.2)  # Aguarda 0.2s
print()
print('\033[1;34mAgora Vamos jogar!\033[m')  # inicia o jogo
print('''\033[1;31m[1]\033[m \033[1mPedra
\033[1;31m[2]\033[m \033[1mPapel
\033[1;31m[3]\033[m \033[1mTesoura
\033[1;31m[4]\033[m \033[1mRegras''')
print()
jog = int(input('\033[1mSelecione uma das opções: \033[m'))  # jogador seleciona uma das opções
print()
if jog == 4:  # Mostra as Regras do Jogo
    print('\033[1mo------------------------o')
    sleep(0.1)
    print('\033[1m|         Regras         |')
    sleep(0.1)
    print('\033[1m|                        |')
    sleep(0.1)
    print('\033[1m| \033[1;31mPapel Ganha de Pedra\033[m   |')
    sleep(0.1)
    print('\033[1m|                        |')
    sleep(0.1)
    print('\033[1m| \033[1;31mPedra Ganha de Tesoura\033[m |')
    sleep(0.1)
    print('\033[1m|                        |')
    sleep(0.1)
    print('\033[1m| \033[1;31mTesoura Ganha de Papel\033[m |')
    sleep(0.1)
    print('\033[1m|                        |')
    sleep(0.1)
    print('\033[1m|                        |')
    sleep(0.1)
    print('\033[1m| \033[1;31mBoa sorte!\033[m             |')
    sleep(0.1)
    print('\033[1mo------------------------o\033[m')
    print()
    sleep(1)  # Aguarda 1s
    input('\033[3;1mPress ENTER to Continue!\033[m')  # Uma pausa até o jogador pressionar ENTER
    sleep(0.2)  # Aguarda 0.2s
    print()
    print('\033[1;34mAgora Vamos jogar!\033[m')  # inicia o jogo
    print('''\033[1;31m[1]\033[m \033[1mPedra
\033[1;31m[2]\033[m \033[1mPapel
\033[1;31m[3]\033[m \033[1mTesoura''')
    print()
    jog = int(input('\033[1mSelecione uma das opções: \033[m'))  # jogador seleciona uma das opções
    print()
    if jog != 1 and jog != 2 and jog != 3:
        print('\033[1;31mSelecione uma opção válida!\033[m')  # Mensagem para opção inválida
        exit()
    pc = randint(1, 3)  # Computador faz uma jogada
    print('\033[1;34mJO\033[m')  # Mensagem de Jo Ken Po
    sleep(0.7)
    print('\033[1;34mKEN\033[m')
    sleep(0.7)
    print('\033[1;34mPO\033[m')
    sleep(0.7)
    print()
    if pc == 1 and jog == 3:
        print('\033[1;31mHaha, Ganhei! Pedra Quebra Tesoura\033[m')  # Mensagem de derrota
    elif pc == 2 and jog == 1:
        print('\033[1;31mHaha, Ganhei! Papel Embrulha Pedra\033[m')  # Mensagem de derrota
    elif pc == 3 and jog == 2:
        print('\033[1;31mHaha, Ganhei! Tesoura Corta Papel\033[m')  # Mensagem de derrota
    elif pc == 1 and jog == 2:
        print('\033[1;32mParabéns, Você Ganhou! Papel Embrulha Pedra\033[m')  # Mensagem de vitória
    elif pc == 2 and jog == 3:
        print('\033[1;32mParabéns, Você Ganhou! Tesoura Corta Papel\033[m')  # Mensagem de vitória
    elif pc == 3 and jog == 1:
        print('\033[1;32mParabéns, Você Ganhou! Pedra Quebra Tesoura\033[m')  # Mensagem de vitória
    else:
        print('\033[1;31mDroga! Deu empate, jogamos a mesma coisa!')  # Mensagem de empate
    exit()
if jog != 1 and jog != 2 and jog != 3:
    print('\033[1;31mSelecione uma opção válida!\033[m')  # Mensagem para opção inválida
    exit()
pc = randint(1, 3)  # Computador faz uma jogada
print('\033[1;34mJO\033[m')  # Mensagem de Jo Ken Po
sleep(0.7)
print('\033[1;34mKEN\033[m')
sleep(0.7)
print('\033[1;34mPO\033[m')
sleep(0.7)
print()
if pc == 1 and jog == 3:
    print('\033[1;31mHaha, Ganhei! Pedra Quebra Tesoura\033[m')  # Mensagem de derrota
elif pc == 2 and jog == 1:
    print('\033[1;31mHaha, Ganhei! Papel Embrulha Pedra\033[m')  # Mensagem de derrota
elif pc == 3 and jog == 2:
    print('\033[1;31mHaha, Ganhei! Tesoura Corta Papel\033[m')  # Mensagem de derrota
elif pc == 1 and jog == 2:
    print('\033[1;32mParabéns, Você Ganhou! Papel Embrulha Pedra\033[m')  # Mensagem de vitória
elif pc == 2 and jog == 3:
    print('\033[1;32mParabéns, Você Ganhou! Tesoura Corta Papel\033[m')  # Mensagem de vitória
elif pc == 3 and jog == 1:
    print('\033[1;32mParabéns, Você Ganhou! Pedra Quebra Tesoura\033[m')  # Mensagem de vitória
else:
    print('\033[1;33mDroga! Deu empate, jogamos a mesma coisa!')  # Mensagem de empate
