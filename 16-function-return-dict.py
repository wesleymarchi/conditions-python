# Retornando um dicionário com idade opcional
def get_person(first_name, last_name, age=''):
    """ Retorna pessoa """
    person = {'first_name': first_name, 'last_name': last_name}

    if age:
        person['age'] = age

    return person


hero = get_person('jardani', 'jovonovich', age=39)
print(hero)