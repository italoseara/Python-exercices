# Variaveis

n = 0
m = 0
r = 's'
maior = 0
menor = 9999999999999999
cont = 1

# Programa

while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [s / n] ')).lower()
    cont += 1
    m = m + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# Saída

print('A media entre todos os números foi de: {:.2f}'.format(m / cont))
print('O maior número dentre todos os digitados foi {}'.format(maior))
print('O menor número dentre todos os digitados foi {}'.format(menor))
