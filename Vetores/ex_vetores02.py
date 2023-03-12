# b) Crie um programa que leia dois vetores e calcule a soma dos elementos correspondentes em cada vetor
from random import randint
import numpy as np

vetor1 = []
vetor2 = []

for i in range(0, 3):
    num = randint(0, 10)
    vetor1.append(num)
    if num in vetor1:
        num = randint(0, 10)
        vetor2.append(num)

print(f'Vetor 1: {vetor1}\nVetor 2: {vetor2}')

x = np.array(vetor1)
y = np.array(vetor2)
soma = x + y
print(f'>> O resultado da soma dos vetores é: {soma}')
