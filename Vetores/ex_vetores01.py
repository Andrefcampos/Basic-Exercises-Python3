# a) Crie um vetor com 10 números inteiros aleatórios e encontre o maior e o menor valor.
from random import randint

vetor = []

for i in range(0, 10):
    numero = randint(0, 99)
    vetor.append(numero)
print(vetor)
print(f'O maior valor do vetor é: {max(vetor)}.')
print(f'O menor valor do vetor é: {min(vetor)}.')
