# b) Crie um programa que leia uma lista e remova os elementos repetidos.

nomes = []

while True:
    nome = str(input('Nome: [Digite "sair" para encerrar] ')).title()
    if nome == 'Sair':
        break
    if nome not in nomes:
        nomes.append(nome)
print(f'Os nomes são: {nomes}')
