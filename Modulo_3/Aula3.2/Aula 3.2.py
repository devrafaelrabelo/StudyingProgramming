#
# Funçoes DEF em Python - RETURN - Aula1.1 (Parte 2)
#

def divisao(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return


divide = divisao(10, 0)

if divide:
    print(divide)
else:
    print('Conta Inválida')

def f(var):
    print(var, 'MEU OVO')

def dumb():
    return f  # Tranforma a variavel em função

var = 11

print(type(var))

var = dumb()

print(type(var))

var('teste')

if var == f:
    print('VAR é igual a F')
else:
    print("Não é")

def dumba():
    return ('Rafael', 'Rabelo')

variavel_1 = dumba()

print(variavel_1, type(variavel_1))

variavel_2 = 'dumba()', 'Rabelo', 'Teste'

print(variavel_2, type(variavel_2))
