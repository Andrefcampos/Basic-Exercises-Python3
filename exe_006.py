num = total = cont = 0
while True:
    num = int(input('Diga um número: '))
    if num == 'end':
        break
    total += num
    cont += 1
    print()
print('ACABOU!')
print(f'O total dos valores foi {float(total)}, a quantidade de valores foi {cont}, a média foi {total/num}')