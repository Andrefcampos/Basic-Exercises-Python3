# d) Crie um programa que leia uma lista e verifique se ela está em ordem crescente.

lista = []

while True:
    num = int(input('Digite um valor: [999 para sair] '))
    if num == 999:
        print('FIM!')
        break
    lista.append(num)
print(lista)
if lista == sorted(lista):
    print('O vetor está em ordem crescente.')
else:
    print('O vetor não está em ordem crescente.')