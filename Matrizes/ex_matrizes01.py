# a) Crie uma matriz de tamanho 3x3 e exiba os valores da diagonal principal.

matriz = []
linhas = 3
colunas = 3
for i in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'Valor de: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz.append(linha)

print(f'>> A diagonal principal é: [{matriz[0][0]}], [{matriz[1][1]}], [{matriz[2][2]}]')
print(f'Matriz: {matriz}')