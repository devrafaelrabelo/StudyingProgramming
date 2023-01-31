#
# Split, Join, Enumerate em Python
# Join - Dividir uma string # STR
# Join - Juntar uma lista # STR
# Enumerate - Enumerar elementos da lista # list / Iteraveis
#

# ----------------------------------------------------------------------------------------------------------------------
# SPLIT
# string = "O Brasil é o país do futebol, o Brasil é penta"
# lista_1 = string.split(' ')
# lista_2 = string.split(',')

# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x) ')


# for valor in lista_2:
#     print(valor.strip().capitalize())  # STRIP para remover espaço do inicio e do final da FRASE.
#                                        # CAPITALIZE Serve para a frase começar com letra maiuscula.
#     # print(valor.strip().title())

# ----------------------------------------------------------------------------------------------------------------------
# # JOIN
# frase = 'O Brasil é penta.'
# lista = frase.split(' ')
# string_2 = ' - '.join(lista)
#
# print(frase)
# print(lista)
# print(string_2)

# # ----------------------------------------------------------------------------------------------------------------------
# # Enumerate
# frase = '0 Brasil é penta.'
# lista = frase.split(' ')
# string_2 = ' - '.join(lista)
# palavra = ''
# for index, valor in enumerate(lista):
#     contagem = 0
#     print(index+1, valor)
#     print("Split")
#
#     for index_1, valor_1 in enumerate(lista[index]):
#         print(index+1, index_1+1, valor_1)
#         qtd_rep_temp = lista[index].count(valor_1)
#
#         if qtd_rep_temp > contagem:
#             contagem = qtd_rep_temp
#             palavra = valor_1
#
#     print(f'--------------  "{palavra}" repetiu {contagem} x')
#
# # ----------------------------------------------------------------------------------------------------------------------
# # Enumerate
# frase = '0 Brasil é penta.'
# lista = frase.split(' ')
# string_2 = ' - '.join(lista)
# palavra = ''
# for index, valor in enumerate(lista):
#     contagem = 0
#     print(index+1, valor)
#     print("Split")
#
#     for valor_1 in lista[index]:
#         print(index+1, valor_1)
#         qtd_rep_temp = lista[index].count(valor_1)
#
#         if qtd_rep_temp > contagem:
#             contagem = qtd_rep_temp
#             palavra = valor_1
#
#     print(f'--------------  "{palavra}" repetiu {contagem} x')
#
# ## print(lista[1][2])

# ----------------------------------------------------------------------------------------------------------------------
# LISTA DE LISTA
# lista_da_lista = [
#     'Rafael',
#     [4, 5, 6],
#     [9, 8, 7],
#     ['A', 'A', 'A'],
#     ['A', 2, True, 8.50],
#     # 8.850, FLOAT NÃO CONSEGUE IMPRIMIR DENTRO
#     # TRUE/FALSE, BOOL NÃO CONSEGUE IMPRIMIR DENTRO
# ]
#
# for v in lista_da_lista:
#     print(v)
#     for b in v:
#         print(b)
#
# lista_da_lista = [
#     ['Rafael', 1.82, 27],
#     ['Rayane', 1.50, 25],
#     ['Roger', 1.80, 30],
#     ['Debora', 1.90, 15],
#     # 8.850, FLOAT NÃO CONSEGUE IMPRIMIR DENTRO
#     # TRUE/FALSE, BOOL NÃO CONSEGUE IMPRIMIR DENTRO
# ]
#
# for nome, altura, idade in lista_da_lista:
#     print(f'Nome: {nome}, \nAltura: {altura:.2f}m, \nIdade: {idade}y\n')


# lista_da_lista = [
#     ['Rafael', 1.82, 27],
#     ['Rayane', 1.50, 25],
#     ['Roger', 1.80, 30],
#     ['Debora', 1.90, 15],
#     # 8.850, FLOAT NÃO CONSEGUE IMPRIMIR DENTRO
#     # TRUE/FALSE, BOOL NÃO CONSEGUE IMPRIMIR DENTRO
# ]
#
# for index, nome, altura, idade in enumerate(lista_da_lista):  #Enumerate funciona somente com 2, indix e valores
#     print(f'{index}: Nome: {nome}, \nAltura: {altura:.2f}m, \nIdade: {idade}y\n')

# lista_da_lista = [
#     ['Rafael', 1.82, 27],
#     ['Rayane', 1.50, 25],
#     ['Roger', 1.80, 30],
#     ['Debora', 1.90, 15],
#     # 8.850, FLOAT NÃO CONSEGUE IMPRIMIR DENTRO
#     # TRUE/FALSE, BOOL NÃO CONSEGUE IMPRIMIR DENTRO
# ]
#
# # for index, nome, altura, idade in enumerate(lista_da_lista):  #Enumerate funciona somente com 2, indix e valores
# for nome, altura, idade in lista_da_lista:
#     print(f'Nome: {nome}, \nAltura: {altura:.2f}m, \nIdade: {idade}y\n')
