s = str(input('Digite uma frase: ')).title()
s1 = s.replace(' ', '').upper()
f = s1[::-1]
print('O inverso de "{}" é "{}"'.format(s1, f))
if s1 == f:
    print('Temos um Palindromo'.format(s))
else:
    print('A frase digitada NÃO é um Palindromo'.format(s))