# d) Crie um programa que leia uma matriz e verifique se ela é uma matriz identidade.

matriz = []
linhas = 3
colunas = 3
for i in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'Valor de: [{i + 1}][{c + 1}] '))
        linha.append(elemento)
    matriz.append(linha)

if matriz[0][0] == 1 and matriz[1][1] and matriz[2][2]:
    print('Esta matriz é uma matriz identidade.')
else:
    print('Esta não é uma matriz identidade.')
print(f'Matriz: {matriz}')