from time import sleep

menu = 0
n1 = int(input('\033[1;34mPrimeiro valor: '))
n2 = int(input('Segundo valor: \033[m'))

while menu != 5:
    print('\033[1;33m{}\033[m \033[1;31mMenu\033[m \033[1;33m{}\033[m'.format('-=-'*15, '-=-'*15))
    print('''    \033[1;31m[1]\033[m \033[1;34mSomar\033[m
    \033[1;31m[2]\033[m \033[1;34mMultiplicar\033[m
    \033[1;31m[3]\033[m \033[1;34mMaior Número\033[m
    \033[1;31m[4]\033[m \033[1;34mDigitar Novos Números\033[m
    \033[1;31m[5]\033[m \033[1;34mSair Do Programa\033[m''')
    menu = int(input('  \033[1;33mDigite Sua Opção: \033[m'))
    sleep(0.1)
    if menu == 1:
        print('\033[1;31mA Soma entre {} e {} é igual a {}\033[m'.format(n1, n2, n1 + n2))
        sleep(1.5)
    elif menu == 2:
        print('\033[1;31m{} x {} é igual a {}'.format(n1, n2, n1 * n2))
        sleep(1.5)
    elif menu == 3:
        if n1 > n2:
            print('\033[1;31mEntre {} e {} o maior número é {}\033[m'.format(n1, n2, n1))
            sleep(1.5)
        elif n2 > n1:
            print('\033[1;31mEntre {} e {} o maior número é {}\033[m'.format(n1, n2, n2))
            sleep(1.5)
        else:
            print('\033[1;31mEntre {} e {} Não exite maior número\033[m'.format(n1, n2))
            sleep(1.5)
    elif menu == 4:
        n1 = int(input('\033[1;34mPrimeiro valor: '))
        n2 = int(input('Segundo valor: \033[m'))
    elif menu == 5:
        print()
        print('\033[1;35mFINALIZANDO...')
        sleep(1.5)
        print()
        print('\033[1;31mAté a proxima! <3\033[m')
    else:
        print('\033[1;31mOpção invalida! Tente Novamente!\033[m')
