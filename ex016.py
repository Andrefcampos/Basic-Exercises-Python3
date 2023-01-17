#Calculadora de custo de aluguel de veículo
#Base de preço quilometragem e dias alugados
#R$60.00 o dia + R$0.15 por km rodado

kmInicial = float(input('Informe a quilometragem do veículo no dia que foi alugado: '))
kmFinal = float(input('Informe a quilometragem do veículo no dia da entrega: '))
dias = int(input('Informe quantos dias o cliente ficou com o veículo: '))

print('-'*15)
print('O veículo passou {:.0f} dias alugado \nPercorreu {:.2f}km \nO total a pagar é R${}'.format(dias, kmFinal-kmInicial, (dias*60)+0.15*(kmFinal-kmInicial)))
print('-'*15)