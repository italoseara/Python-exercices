vel = float(input('Velocidade atual do carro: '))  # Pergunta a velocidade do carro
print()
if vel <= 80:
    print('\033[1;32mTenha um bom dia e dirija com precaução!')  # Carro dentro do limite de velocidade
else:
    print('\033[1;31mVocê está acima do limite permitido!')  # Carro fora do limite de velocidade
    multa = (vel - 80) * 7  # Calcula a multa
    print('\033[1;31mSua multa sairá no valor de R${:.2f}'.format(multa))  # Indica o preço da multa
