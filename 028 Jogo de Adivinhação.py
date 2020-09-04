from random import randint
from time import sleep

print()
print('\033[1;33m-=-\033[m'*30)
print('\033[1;34mVamos jogar um joguinho! vou pensar em um número de 0 a 5 e você tenta advinhar!\033[m')
print('\033[1;33m-=-\033[m'*30)
pc = randint(0, 5)  # Computador Pensa no número
sleep(0.3)  # Aguarda 0.3s

jog = int(input('Qual número você acha que eu pensei? '))  # Jogador tenta advinhar
print()
sleep(0.3)  # Aguarda 0.3s

print('Vamos ver se conseguiu acertar!')
sleep(0.5)  # Aguarda 0.5s

print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)  # Aguarda 2s

if jog == pc:
    print('\033[1;32mPARABÉNS! Você ganhou! Eu pensei em {}\033[m'.format(pc))  # Mensagem de vitória
else:
    print('\033[1;31mERROU! Eu pensei em {}\033[m'.format(pc))  # Mensagem de derrota
