# c) Crie um programa que leia um vetor e um número inteiro k e exiba os k primeiros elementos do vetor.
vetor = [1, 3, 5, 7, 5, 4, 3, 4, 8, 10]
k = int(input('Deseja visualizar quantas posições do vetor? '))

if k <= len(vetor):
    for i in range(0, k):
        print(f'{vetor[i]}, ', end='')
    print('Fim!')
else:
    print(f'{k} é um valor fora do intervalo do vetor. Tente novamente')
