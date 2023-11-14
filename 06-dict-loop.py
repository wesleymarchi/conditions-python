# loop em dicionario

heros = {
    'batman': 'python',
    'superman': 'java',
    'rorschach': 'javascript',
}

for hero, language in heros.items():
    print("Hero: " + hero.title())
    print("Language: " + language.title() + "\n")
