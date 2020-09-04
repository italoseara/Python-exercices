while True:
    num = int(input('\033[30mQuer ver a tabuada de qual valor?: '))
    if num < 0:
        break
    n = 0
    print('\033[1;31m-\033[m' * 15)
    while n != 10:
        n += 1
        print(f'\033[1;30m{num} x {n} = {num * n}\033[m')
    print('\033[1;31m-\033[m' * 15)
