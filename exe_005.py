menor = None
print('Antes')
for valor in [9, 2, 14, 50, 23]:
    if menor == None:
        menor = valor
    elif valor < menor:
        menor = valor
    print(menor, valor)
print('Depois', menor)