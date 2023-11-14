# loop while

heros = []
active = True  # flag

while active:
    name = input("Insira o nome de um heroi. (S para sair)\n")

    if name.lower() == 's':
        active = False
    else:
        heros.append(name)
        print(name.title())

print("Sua lista de herois: ")
print(heros)
