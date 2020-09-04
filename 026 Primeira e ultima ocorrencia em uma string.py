frase = str(input('Digite uma Frase: ')).lower().strip()
print('A letra "a" aparece \033[1;34m{}\033[m vezes na frase'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição \033[1;34m{}\033[m'.format(frase.find('a') + 1))
print('A letra "a" aparece pela ultima vez na posição \033[1;34m{}\033[m'.format(frase.rfind('a') + 1))