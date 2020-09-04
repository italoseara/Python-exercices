casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = float(input('Parcelas (Anos): '))
prest = casa / anos
print()
if prest < sal * 30 / 100:
    print("""Desculpe, mas nao podemos aprovar seu empréstimo! 
Pois, ele excede 30% do salário do comprador.""")
else:
    print('Empréstimo aprovado! Total: R${:.2f}'.format((prest - sal) * anos))