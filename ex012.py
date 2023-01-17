alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual a largura da sua parede?'))

print('Sua parede mede {:.2f}mx{:.2f}m e sua área é de {:.2f}m² \nserá necessário {:.2f}L de tinta'.format(alt, larg, alt*larg, (larg*alt)/2))