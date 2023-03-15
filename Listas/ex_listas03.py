# c) Crie um programa que leia uma lista de números e exiba apenas os números pares.
lista = []
listaPar = []
while True:
    num = int(input('Digite um valor: '))

    if num != 0:
        if num % 2 == 0:
            listaPar.append(num)
    if num == 999:
        break
    lista.append(num)
lista.sort()
print('-' * 40)
print(f'Os números foram: {lista}')
print(f'Destes números, os pares foram: {listaPar}')