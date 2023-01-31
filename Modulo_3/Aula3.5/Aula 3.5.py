#
# Funçoes (DEF) em python - *args **kwargs
#

# lista = [1, 2, 3, 4, 5]
# print(*lista, sep="")

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(args[4])
#     print(args[5], '\n')
#     print(args[-1])
#     print(args[-2])
#     print(args[-3])
#     print(args[-4])
#     print(args[-5])
#     print(args[-6], '\n')
#     print(len(args))
#
#
#
# func(1, 2, 3, 4, 5, 6)



# def func_1(*args):
#     print(type(args))
#     print(args)
#     #  args[0] = 1
#     args = list(args)
#     print(type(args))
#     print(args)
#     print(args[0])
#     args[0] = 10
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(args[4])
#     print(args[5], '\n')
#     print(args[-1])
#     print(args[-2])
#     print(args[-3])
#     print(args[-4])
#     print(args[-5])
#     print(args[-6], '\n')
#     print(len(args))
#
#
#
# func_1(1, 2, 3, 4, 5, 6)

# def func_1(*args):
#     print(type(args))
#     print(args)
#     #  args[0] = 1
#     args = list(args)
#     print(type(args))
#     print(args)
#     print(args[0])
#     args[0] = [10, 20, 30, 40, 50]
#     print(*args[0])
#     print(args[1])
#     # print(args[2])
#     # print(args[3])
#     # print(args[4])
#     # print(args[5], '\n')
#     print(args[-1])
#     print(args[-2])
#     # print(args[-3])
#     # print(args[-4])
#     # print(args[-5])
#     # print(args[-6], '\n')
#     print(len(args))
#
#
# lista = [1, 2, 3, 4, 5, 6]
# lista2 = [11, 22, 33, 44, 55, 66]
#
# func_1(*lista, *lista2)
#
# #  func_1(lista, 1, 2, 3, 4, 5)

# def func_1(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#     print(args, kwargs)
#     #  args[0] = 1
#     args = list(args)
#     print(type(args))
#     print(args)
#     print(args[0])
#     args[0] = [10, 20, 30, 40, 50]
#     print(*args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(args[4])
#     print(args[5], '\n')
#     print(args[-1])
#     print(args[-2])
#     print(args[-3])
#     print(args[-4])
#     print(args[-5])
#     print(args[-6], '\n')
#     print(len(args))
#     print(kwargs)
#     print(kwargs['nome'])
#     print(kwargs['sobrenome'])
#     print(len(kwargs['nome']))
#     print(len(kwargs['sobrenome']))
#     print(len(kwargs))
#
# lista = [1, 2, 3, 4, 5, 6]
# lista2 = [11, 22, 33, 44, 55, 66]
#
# func_1(*lista, *lista2, nome='Rafael', sobrenome='Rabelo')
#
# #  func_1(lista, 1, 2, 3, 4, 5)

def func_1(*args, **kwargs):
    print(args)
    print(*kwargs['nome'])
    print(f"{kwargs.get('nome')}")
    idade = kwargs.get('idade')
    print(f"{kwargs.get('idade')}")

    if idade is not None:
        print(*kwargs["nome"], kwargs["sobrenome"], 'tem ', idade, "anos")
    else:
        print("Não mandou idade")


lista = [1, 2, 3, 4, 5, 6]
lista2 = [11, 22, 33, 44, 55, 66]
lista_nome = 'Rafael', "Rabelo"

func_1(*lista, *lista2, nome=lista_nome, sobrenome='Gonçalves', idade=27)

#  func_1(lista, 1, 2, 3, 4, 5)
