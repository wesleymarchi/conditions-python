# Estrutura if..elif..else

heros = ['batman', 'superman', 'spiderman', 'rorschach']
print(heros)

x = 5
y = 10
z = x > 10

if z:  # inserir not
    print(str(x) + ' é maior que ' + str(y))

hero = heros[-1].lower()

if hero == 'superman':
    print('Voa super!')
elif hero == 'spiderman':
    print('Vai teia!')
elif hero == 'batman':
    print('Vai morcegão!')
else:
    print('Heroi ou vilão?')
