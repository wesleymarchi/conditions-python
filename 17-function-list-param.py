# Lista como parâemtro
def welcome(heros):
    """ Saudação para uma lista de herois """
    for hero in heros:
        message = "Hello, " + hero.title()
        print(message)


heros = ['rorschach', 'batman', 'homelander']
welcome(heros)
