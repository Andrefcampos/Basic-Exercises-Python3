din = float(input('Digite quanto você tem na carteira: '))
dol = float(input('Digite a cotação do dólar hoje: '))

print('Você possui R${:.2f} na carteira e em dólares vale US${:.2f} hoje'.format(din, din/dol))
