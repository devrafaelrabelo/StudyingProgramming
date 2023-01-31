#
# 1 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada
#
def func_1_1(msg):
    return msg


def func_1_2():
    return 10


print(func_1_1(func_1_2()), '\n')


#
# 2 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada.
# Faça a função1 executar duas funçoes que recebam um numero diferente de argumentos.

def func_2_1(num):
    lista_1 = [1, 2]
    lista_2 = [3, 4]
    lista_3 = [5, 6]

    return (func_2_3(lista_1, lista_2) * func_2_4(lista_1, lista_2, lista_3)) / num


def func_2_2():
    return 2


def func_2_3(*args):
    soma = 0
    for i in args[0]:
        for x in args[1]:
            soma = soma + (i*x)

    return soma


def func_2_4(*args):
    soma = 0
    for i in args[0]:
        for x in args[1]:
            for y in args[2]:
                soma = soma + (i*x*y)

    return soma


print(func_2_1(func_2_2()))
