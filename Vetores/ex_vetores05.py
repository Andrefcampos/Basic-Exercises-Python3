# e) Crie um programa que leia um vetor e verifique se ele contém um elemento específico.
from random import randint
from time import sleep

vetor = []

for i in range(0, 5):
    num = randint(0, 10)
    vetor.append(num)
pergunta = int(input('Qual número deseja encontrar no vetor? [0 - 10] '))
sleep(1)
if pergunta in vetor:
    print(f'>> O número {pergunta} está contido no vetor.')
    print('-'*40)
else:
    print(f'>> O número {pergunta} não está contido no vetor.')
    print('-'*40)
sleep(1)
print(f'Vetor: {vetor}')
