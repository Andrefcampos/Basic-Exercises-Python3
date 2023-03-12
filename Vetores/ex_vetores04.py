# d) Crie um programa que leia um vetor e verifique se ele está em ordem crescente.
from random import randint

vetor = []

for i in range(0, 6):
    num = randint(0, 99)
    vetor.append(num)
print(vetor)
if vetor == sorted(vetor):
    print('O vetor está em ordem crescente.')
else:
    print('O vetor não está em ordem crescente.')