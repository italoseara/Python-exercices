# Variaveis

n = 0
m = 0
maior = 0
menor = 9999999999999999
cont = 0

# Programa

while cont != 5:
    n = int(input('Digite o peso de uma pessoa: '))
    cont += 1
    m = m + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# Saída

print('O maior peso dentre todos os digitados foi {}'.format(maior))
print('O menor peso dentre todos os digitados foi {}'.format(menor))
