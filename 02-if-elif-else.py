# Estrutura if..elif..else

heros = ['batman', 'superman', 'spiderman', 'rorschach']
print(heros)

x = 5
y = 10
z = x > 10

if (x >= 5) and (y <= 10):
    print('x: ' + str(x) + '\ny: ' + str(y))

if (x > 5) or (y > 5):
    print('Um dos valores é maior que 5.')

if z:  # false
    print(str(x) + ' é maior que ' + str(y))

if not z:  # true
    print(str(x) + ' é maior que ' + str(y) + '?')

hero = heros[-1].lower()

if hero == 'superman':
    print('Voa super!')
elif hero == 'spiderman':
    print('Vai teia!')
elif hero == 'batman':
    print('Vai morcegão!')
else:
    print('Heroi ou vilão?')
