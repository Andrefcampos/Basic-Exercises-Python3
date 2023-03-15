# a) Crie uma lista com alguns nomes e ordene a lista em ordem alfabética
nomes = []
while True:
    nome = str(input('Nome: [Digite "sair" para finalizar] ')).title()
    if nome == 'Sair':
        break
    nomes.append(nome)
print(sorted(nomes))
