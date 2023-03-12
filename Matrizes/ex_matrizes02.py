# b) Crie um programa que leia duas matrizes e calcule a soma das duas

matriz1 = []
matriz2 = []
linhas = 2
colunas = 2

print('-'*40)
print(f'{"SOMA ENTRE MATRIZES":^40}')
print('-'*40)

for i in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'Valor de M1: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz1.append(linha)
print('-'*40)
for i in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'Valor de M2: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz2.append(linha)

soma_matrizes = []
for i in range(linhas):
    linha = [0]*colunas
    soma_matrizes.append(linha)
    for c in range(colunas):
        soma_matrizes[i][c] = matriz1[i][c] + matriz2[i][c]

print('-'*40)
print(f'Matriz 1: {matriz1}')
print(f'Matriz 2: {matriz2}')
print('-'*40)
print(f'>> A soma das matrizes foi: {soma_matrizes}')
