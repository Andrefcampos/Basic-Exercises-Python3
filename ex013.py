price = float(input('Coloque o preço do produto: R$'))
off = price - (price * 5 / 100)

print('O produto custa R${} e com 5% de desconto sai por R${}'.format(price, off))