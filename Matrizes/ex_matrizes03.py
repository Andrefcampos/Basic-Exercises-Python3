# c) Crie um programa que leia uma matriz e calcule a transposta da matriz.

matriz1 = []
matriz2 = []
linhas = colunas = 0

print('-' * 40)
print(f'{"SOMA ENTRE MATRIZES":^40}')
print('-' * 40)

linhas1 = int(input('Numero de linhas: '))
colunas1 = int(input('Numero de colunas: '))
for i in range(linhas1):
    linha = []
    for c in range(colunas1):
        elemento = int(input(f'Valor de M1: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz1.append(linha)
print('-' * 40)

linhas2 = int(input('Numero de linhas: '))
colunas2 = int(input('Numero de colunas: '))
for i in range(linhas2):
    linha = []
    for c in range(colunas2):
        elemento = int(input(f'Valor de M2: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz2.append(linha)

soma_matrizes = []
for i in range(linhas):
    linha = [0] * colunas
    soma_matrizes.append(linha)
    for c in range(colunas):
        soma_matrizes[i][c] = matriz1[i][c] + matriz2[i][c]

print('-' * 40)
print(f'Matriz 1: {matriz1}')
print(f'Matriz 2: {matriz2}')
print('-' * 40)
print(f'>> A soma das matrizes foi: {soma_matrizes}')