n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif 5 < m < 7:
    print('\033[1;31mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')
