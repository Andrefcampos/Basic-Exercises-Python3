num = total = cont = soma = 0
while True:
    num = input('Diga um número: ')
    if num == 'end':
        break
    try:
        total = float(num)
        cont += 1
        soma += total
    except:
        print('Erro na formataçao. Tente novamente.')
        continue
print('ACABOU!')
print(f'O total dos valores foi {soma}, a quantidade de valores foi {cont}, a média foi {soma/cont}')
