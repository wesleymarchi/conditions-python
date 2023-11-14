# Função com retorno
def get_full_name(first_name, last_name):
    """ Retorna o nome completo """
    full_name = first_name + ' ' + last_name
    return full_name.title()


hero = get_full_name('iron', 'man')
print(hero)
