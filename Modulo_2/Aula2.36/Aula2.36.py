#
# Listas em Python
# fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range


booleanos = True  # True ou False
inteiros = 10  # Numeros inteiros
flutuante = -10.10  # NUmeros com pontos ou virgulas
string = 'TEXTO ou LETRA'  # Letras ou Palavras
lista = ['RAFAEL RABELO']

# ----------------------------------------------------------------------------------------------------------------------
#         0         1    2    3    4    5
# lista = ['Rafael', 'A', 'F', 'A', 'E', 'L']
#         6         5    4    3    2    1

# string = "RAFAEL"

print(lista[0])
print(string[0])


# ----------------------------------------------------------------------------------------------------------------------
#         0         1    2    3    4    5
lista = ['Rafael', 'A', 'F', True, 'E', 0.2]
#         6         5    4    3    2    1

string = "RAFAEL"

print(lista)
print(string[0])

for n in lista:
    print(f'{n} = {type(n)}')


# ----------------------------------------------------------------------------------------------------------------------
#         0         1    2    3    4    5
lista = ['Rafael', 'A', 'F', True, 'E', 0.2]
#         6         5    4    3    2    1
print("LISTA")
print(lista[2:5])
print(f'{lista[0:2]} {type(lista[2:5])}')
print(lista[::2])
print(lista[::-1])


print("\nSTRING")
string = "RAFAEL"
print(string[0:2])
print(f'{string[0:2]} {type(string[2:5])}')

# ----------------------------------------------------------------------------------------------------------------------
l1 = [1, 2, 3]
print(l1)

l2 = [4, 5, 6]
print(l2)

# CONCATENAR
l3 = l1 + l2
print(l3)

# EXTEND - EXTENDER
l4 = [-2, -1, 0]
print(l4)
l4.extend(l3)
print(l4)
n = 7
# l4.extend('7')  # EXTEND não aceita INT
# l4.extend(True)  # EXTEND não aceita BOOL
# l4.extend('7')  # Aceita apenas STRING
print(l4)

# INSERT - INSERIR
l4.insert(4, '1.5')
print(l4)

# POP - RETIRAR
l4.pop(4)
print(l4)

# DEL - EXCLUIR
del(l4[0:3])
print(l4)

# MAX - MIN
print(max(l4), min(l4))

# RANGE - LIST
l5 = range(1, 9)
print(l5)

l5 = list(range(0, 10, 1))
print(l5)

# for valor in l5:
#     print(valor)

print('SOMA')
soma = 0

for valor in l5:
    soma += valor
    print(f'{soma-valor} + {valor} = {soma}')

print(soma)

l6 = [2, 5, True, False, 20.2, 2.5555555, 'RAFAEL']
for elem in l6:
    print(f'O tipo do elemento é {type(elem)} e seu valor é {elem}')
