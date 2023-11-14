# Dicionário dentro de outro dicionário
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'churchill': {
        'first': 'winston',
        'last': 'churchill',
        'location': 'reino unido',
    },

    'thatcher': {
        'first': 'margaret',
        'last': 'thatcher',
        'location': 'reino unido',
    },

    'stalin': {
        'first': 'josef',
        'last': 'stalin',
        'location': 'urss',
    },
}

for username, info in users.items():
    print("\nUsername: " + username)
    full_name = info['first'] + " " + info['last']
    location = info['location']

    print("\tFull name: " + full_name.title())
