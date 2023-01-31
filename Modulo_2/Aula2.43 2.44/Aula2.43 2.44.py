#
# Desafio dos contadores
#

cont1 = 0
cont2 = 10

while cont2 >= 2:
    print(cont1, cont2)
    cont1 = cont1 + 1
    cont2 = cont2 - 1

print('')

for r in range(10, 1, -1):
    print(10-r, r)

print('')

for i, r in enumerate(range(10, 1, -1)):
    print(i, r)
