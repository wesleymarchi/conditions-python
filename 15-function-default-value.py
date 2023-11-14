# Função com retorno
def get_full_name(first_name, last_name, middle_name=''):
    """ Retorna o nome completo """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


hero = get_full_name('john', 'wick', 'jovonovich')
print(hero)
