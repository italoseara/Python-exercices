from random import randint
from time import sleep

print('\033[1;33m-=-\033[m'*30)
print('\033[1;34mVamos jogar um joguinho! vou pensar em um número de 0 a 5 e você tenta advinhar!\033[m')
print('\033[1;33m-=-\033[m'*30)  # Mensagem incial
pc = randint(0, 5)  # Computador Pensa no número
sleep(0.3)  # Aguarda 0.3s

jog = int(input('\033[1mQual número você acha que eu pensei? \033[m'))  # Jogador tenta advinhar
print()
sleep(0.3)  # Aguarda 0.3s

print('\033[1;35mPROCESSANDO...\033[m')  # Mensagem de "Processando..."
sleep(2)  # Aguarda 2s
print()

cont = 1
while pc != jog:
    print('\033[1;31mERROU! Tente Novamente!\033[m')
    print()
    jog = int(input('\033[1mQual número você acha que eu pensei? \033[m'))  # Jogador tenta novamente
    cont += 1

print()
print('\033[1;32mPARABÉNS! Você ganhou! Eu pensei em {}\033[m'.format(pc))  # Mensagem de vitória
print('\033[1;34mVocê precisou de {} tentativas para acertar!'.format(cont))  # Mensagem de tentativas
