# Valores default: devem ser utilizados sempre ao fim da lista de parâmetros
def describe_hero(team, hero='batman'):
    """ Exibe o time do heroi e seu nome """
    print("\nTeam: " + team.title())
    print("Hero: " + hero.title())


describe_hero('squad')
describe_hero(team='rorschach')
describe_hero(team='rorschach', hero='spiderman')
