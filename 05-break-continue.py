# Break é uma instrução para sair de um fluxo/loop

heros = []
active = True
while active:
    hero = input("Insira o nome de um heroi (S para sair) \n")

    if hero.lower() == 's':
        break
    else:
        heros.append(hero)
        print("Heroi inserido com sucesso...\n\t" + hero.title())

print("Sua lista de herois: ", heros)
print("\n++++++++++++++++++++++++++++\n")

# Continue é uma instrução que permite continuar o fluxo do código normalmente
x = 0
while x < 10:
    if x % 2 == 0:
        print("[" + str(x) + "]" + " Estou na condição do 'continue'")
        print("\tx = " + str(x) + "\n")
        x += 1
        continue
    else:
        x += 1
