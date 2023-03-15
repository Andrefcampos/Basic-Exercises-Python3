# e) Crie um programa que leia uma lista e crie uma nova lista com os elementos da lista original, mas sem os elementos repetidos.

lista = []
lista_unica = []
while True:
    try:
        valor = int(input('Digite um valor:[999 p/ encerrar] '))
    except:
        valor = 0
    if valor == 999:
        break
    if valor not in lista:
        lista_unica.append(valor)
    lista.append(valor)
print('-'*40)
print(f'Lista principal: {sorted(lista)}')
print(f'Lista sem repetições: {sorted(lista_unica)}')