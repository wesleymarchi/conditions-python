# Argumentos nomeados podem ser passados em qualquer ordem
def describe_hero(team, hero):
    """ Exibe o time do heroi e seu nome """
    print("\nTeam: " + team.title())
    print("Hero: " + hero.title())


describe_hero(hero='rorschach', team='Watchmen')
