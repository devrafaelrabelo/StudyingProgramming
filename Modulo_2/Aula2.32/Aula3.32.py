#
# While em Python
# utilizando para realizar açoes enquanto
# uma condição for verdadeira

# Requisitos: Entender condições e operadores

# Exemplo - 1 Loop Infinito
# while True:
#     nome = input("Digite seu nome: ")
#     print(f'Olá {nome}')
#
# print("Nunca sera executada.")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 2
# x = 0
# while x <= 100:
#     print(x)
#     x = x + 1
# print("Acabou")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 3 - CONTINUE
# x = 1
# while x <= 100:
#     if  x % 2:
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1
# print("Acabou")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 3 - BREAK
# x = 1
# while x <= 100:
#     if x == 50:
#         print(x)
#         break
#     print(x)
#     x = x + 1
# print("Acabou")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 4
# x = 0
# y = 0
# while x < 10:
#     print(x)
#     x += 1  # x = x + 1
# print("Acabou")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 5
# x = 0
# while x < 10:
#     y = 0
#     print(f'Coluna {x}')
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1
#     x += 1  # x = x + 1
#
# print("Acabou")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 6 - Calculadora
# while True:
#     print(f'Escreva o numero ou digite ou digite "sair".')
#     num_1 = input("Digite o 1º numero: ")
#
#     while not num_1.isdigit():
#         print("Dados Invalidos!")
#         num_1 = input("Digite o 1º numero: ")
#         if num_1 == 'sair':
#             break
#     if num_1 == 'sair':
#         break
#     num_1 = int(num_1)
#
#     num_2 = input("Digite o 2º numero: ")
#     if num_2 == 'sair':
#         break
#     while not num_2.isdigit():
#         print("Dados Invalidos!")
#         num_2 = input("Digite o 2º numero: ")
#         if num_2 == 'sair':
#             break
#     if num_2 == 'sair':
#         break
#     num_2 = int(num_2)
#
#     operador = input("Digite o operador: ")
#     if operador == 'sair':
#         break
#     while not operador == '+' and not operador == '-' and not operador == '/' and not operador == '*':
#         print('Operado Errado')
#         operador = input("Digite um operado (+, -, /, *): ")
#         if operador == 'sair':
#             break
#     if operador == 'sair':
#         break
#
#     if operador == '+':
#         print(f'{num_1} {operador} {num_2}: {num_1+num_2}')
#     elif operador == '-':
#         print(f'{num_1} {operador} {num_2}: {num_1-num_2}')
#     elif operador == '/':
#         print(f'{num_1} {operador} {num_2}: {num_1/num_2}')
#     elif operador == '*':
#         print(f'{num_1} {operador} {num_2}: {num_1*num_2}')

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo — 6 - Calculadora

while True:
    print(f'Calculadora.')
    num_1 = input("Digite o 1º numero: ")
    while not num_1.isdigit():
        print("Dados Invalidos!")
        num_1 = input("Digite o 1º numero: ")
    num_1 = int(num_1)

    num_2 = input("Digite o 2º numero: ")
    while not num_2.isdigit():
        print("Dados Invalidos!")
        num_2 = input("Digite o 2º numero: ")
    num_2 = int(num_2)

    operador = input("Digite o operador: ")
    while not operador == '+' and not operador == '-' and not operador == '/' and not operador == '*':
        print('Operado Errado')
        operador = input("Digite um operado (+, -, /, *): ")

    if operador == '+':
        print(f'{num_1} {operador} {num_2}: {num_1+num_2}')
    elif operador == '-':
        print(f'{num_1} {operador} {num_2}: {num_1-num_2}')
    elif operador == '/':
        print(f'{num_1} {operador} {num_2}: {num_1/num_2}')
    elif operador == '*':
        print(f'{num_1} {operador} {num_2}: {num_1*num_2}')

    sair = input('Deseja sair? [S]im [N]ão: ')
    if not sair == 'S':
        break
    else:
        continue