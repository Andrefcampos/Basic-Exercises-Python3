name = str(input('Diga seu nome: '))
lang = str(input('Em qual liguagem você deseja receber a saudação? [en/pt/fr/es] ')).strip().lower()
def greet(lang):
    if lang == 'en':
        return 'Hello'
    elif lang == 'br':
        return 'Olá'
    elif lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Olá'
print('{}, {}!'.format(greet(lang), name))