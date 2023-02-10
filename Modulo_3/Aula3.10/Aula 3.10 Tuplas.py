""""""
"""
Tuplas 

- Tuplas nao pode ter seu valor alterado e nao pode ser inserido dados
"""
print("\n--------- Tuplas com PARENTESES ---------")

t1 = (1, 2, 3, 'a', 'Rafael Rabelo')

print(t1, ' - ', type(t1))

for v in t1:
    print(v)

print(t1[1:])

print("\n--------- Tuplas sem PARENTESES ---------")

t2 = 2, 3, 'a', 'Rafael Rabelo', 'Carlos'

print(t2, ' - ', type(t2))

for v in t2:
    print(v)

print(t2[1:])

print("\n--------- Tuplas criação ---------")

print("\n--------- Criar tupla sem virgula, da erro e vira um INT ---------")
t3 = 1
print(t3, ' - ', type(t3))

print("\n--------- Necessario colocar a virgula para criação da TUPLA ---------")
t4 = (1,) * 20
print(t4, ' - ', type(t4))

print("\n--------- Concatenar Tuplas ---------")
t5 = t4 + t2
print(t5, ' - ', type(t5))

print("\n---------  Desempacotar Tuplas ---------")

n1, n2, n3, n4, *_, n6 = t5

print(n2)
print(n6)

print("\n---------  Modificar Tuplas (Transforma em lista e depois voltar) ---------")

t5 = list(t5)
print(t5[24], type(t5))

t5 = tuple(t5)
print(t5[24], type(t5))
