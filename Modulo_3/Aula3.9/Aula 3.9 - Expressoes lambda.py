""""""
"""
Funções Anonimas - LAMBDA
"""
print("--------- Exemplo da Função Normal ---------")


def func(arg, arg2):
    return arg * arg2


var = func(2, 2)

print(var)

print("\n--------- Exemplo da Função Lambda(Anonima) ---------")

a = lambda x, y: x * x

print(a(2, 2))

print("\n--------- Exemplo da Função sem Lambda - 1 ---------")
lista = [
    ['Produto_1', 80],
    ['Produto_3', 50],
    ['Produto_2', 12],
    ['Produto_5', 60],
    ['Produto_4', 11]
]
print(lista, '\n')


def func(item):
    return item[1]


lista.sort(key=func)
print(lista)

lista.sort(key=func, reverse=True)
print(lista, '\n')


def func_1(item):
    return item[0]


lista.sort(key=func_1)
print(lista)

lista.sort(key=func_1, reverse=True)
print(lista)

print("\n--------- Exemplo da Função Lambda(Anonima) - 1 (Muda a Lista Original)---------")
lista.sort(key=lambda item: item[0], reverse=True)
print(lista)

lista.sort(key=lambda item: item[0])
print(lista)

print("\n--------- Exemplo da Função Lambda(Anonima) - 2 (Muda a Lista Original)---------")
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

lista.sort(key=lambda item: item[1])
print(lista)

print("\n--------- Exemplo da Função Lambda(Anonima) - 3 (usando o Metodo Sorted, que nao muda a Lista Original)---------")
print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[1], reverse=True), '\n')

print(sorted(lista, key=lambda i: i[0]))
print(sorted(lista, key=lambda i: i[0], reverse=True), '\n')

print(lista)
