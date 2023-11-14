# Dicionário com os planetas
planets = {
    'mercurio': {
        'temperature': 179,
    },

    'venus': {
        'temperature': 464,
    },

    'terra': {
        'temperature': 15,
    },

    'marte': {
        'temperature': -40,
    },

    'jupiter': {
        'temperature': -120,
    },

    'saturno': {
        'temperature': -180,
    },

    'urano': {
        'temperature': -210,
    },

    'netuno': {
        'temperature': -210,
    },
}

for planet, temperature in planets.items():
    value = temperature['temperature']
    print("\nPlaneta: " + planet.title())
    print("\tTemperatura: " + str(value))
