# Passando um número arbitrario de argumentos
def heros(*list_heros):
    """ Exibe uma lista de herois. """
    for hero in list_heros:
        print(hero)


heros('batman')
heros('rorschach', 'joker', 'homelander')
