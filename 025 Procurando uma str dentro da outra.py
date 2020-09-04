nome = str(input('Seu nome completo: '))
nome = nome.lower().strip()
print('Seu nome tem Silva? \033[1;34m{}'.format('silva' in nome))
