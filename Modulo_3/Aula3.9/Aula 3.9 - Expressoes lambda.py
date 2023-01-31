#
# Funções Anonimas - LAMBDA
#

# def func(arg, arg2):
#     return arg * arg2
#
# var = func(2, 2)
#
# print(var)
#
#
# a = lambda x, y: x * x
#
# print(a(2,2))

lista = [
    ['Produto_1', 80],
    ['Produto_2', 12],
    ['Produto_3', 50],
    ['Produto_5', 1654],
    ['Produto_4', 11]
]
# print(lista)

# def func(item):
#     return item[1]
#
# lista.sort(key=func)
#
# print(lista)
#
# lista.sort(key=func, reverse=True)
#
# print(lista)

# lista.sort(key=lambda item:  item[0], reverse=True)
# print(lista)
#
# lista.sort(key=lambda item:  item[0])
# print(lista)
#
# lista.sort(key=lambda item:  item[1], reverse=True)
# print(lista)
#
# lista.sort(key=lambda item:  item[1])
# print(lista)

print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[1], reverse=True))
print(sorted(lista, key=lambda i: i[0]))
print(sorted(lista, key=lambda i: i[0], reverse=True))
