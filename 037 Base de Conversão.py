num = int(input('Digite um número inteiro qualquer: '))
print()
print('''1 - Binário
2 - Octal
3 - Hexadecimal''')
bc = int(input('Selecione a Base de conversão: '))
if bc == 1:
    print('O número {} em Binário será representado por: {}'.format(num, bin(num)[2:]))
elif bc == 2:
    print('O número {} em Octal será representado por: {}'.format(num, oct(num)[2:]))
elif bc == 3:
    print('O número {} em Hexadecimal será representado por: {}'.format(num, hex(num)[2:]))
else:
    print('Selecione um número que represente uma base de conversão!')