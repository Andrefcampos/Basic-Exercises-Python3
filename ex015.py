#Conversor de temperatura de °C a °F

temp = float(input('Informa a temperatura em °C: '))

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(temp, (9*temp)/5+32))