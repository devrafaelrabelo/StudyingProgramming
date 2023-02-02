""""""
"""
Funçoes (DEF) em python - *args **kwargs
"""
print("---------------------------------------------------------------------------------------------------------------")
print("--------- INICIO DE *ARGS ---------")

lista = [1, 2, 3, 4, 5]
print(*lista, sep=" - ")
print(lista)
print("----------------------------------------------------------")


def func(*args):
    print(args, '\n')
    print("Impressão dos dados Crescente")
    for i in range(len(args)):
        print(args[i])

    print("\nImpressão dos dado Decrescente")
    for i in range(len(args), 0, -1):
        print(args[i - 1])

    print("\nTamanho: ", len(args))


print("\nEnviando Separadamente")
func(1, 2, 3, 4, 5, 6)
print("----------------------------------------------------------")

print("Enviando Empacotada")
lista = 1, 2, 3, 4, 5
func(lista, '6')
print("----------------------------------------------------------")

print("Enviando Desempacotada")
lista = 1, 2, 3, 4, 5
func(*lista, '6')
print("----------------------------------------------------------")

print("----------------------------------------------------------")
print("Verificando com listas")
print("Lista 1")
lista = [1, 2, 3, 4, 5, 6]
print(type(lista))

print("Lista 2")
lista2 = [11, 22, 33, 44, 55, 66]
print(type(lista2))
print("----------------------------------------------------------")

print("Enviando Duas Lista Empacotada")
func(lista, lista2)
print("----------------------------------------------------------")

print("Enviando Duas Lista Desempacotada")
func(*lista, *lista2)
print("----------------------------------------------------------")

print("Enviando Uma Lista Desempacotada | Uma Lista Empacotada")
func(*lista, lista2)
print("----------------------------------------------------------")
print("---------- FINAL DE *ARGS ---------")
print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")
print("--------- INICIO DE *KWARGS ---------")
def func_1(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    teste = list(args)
    print(type(teste))
    print(teste)
    print(teste[0])
    teste[0] = [10, 20, 30, 40, 50]
    print(teste[0])
    print(teste[1])
    print(teste[2])
    print(teste[3])
    print(teste[4])
    print(teste[5])
    print(teste[6], '\n')
    print(args[-1])
    print(args[-2])
    print(args[-3])
    print(args[-4])
    print(args[-5])
    print(args[-6], '\n')
    print(len(args))
    print(kwargs)
    print(kwargs['nome'])
    print(kwargs['sobrenome'])
    print(len(kwargs['nome']))
    print(len(kwargs['sobrenome']))
    print(len(kwargs))


print("----------------------------------------------------------")
print("Lista 1")
lista = [1, 2, 3, 4, 5, 6]
print(type(lista))

print("Lista 2")
lista2 = [11, 22, 33, 44, 55, 66]
print(type(lista2))
print("----------------------------------------------------------")

func_1(*lista, *lista2, nome='Rafael', sobrenome='Rabelo')


def func_2(*args, **kwargs):
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

func_2(*lista, *lista2, nome=lista_nome, sobrenome='Gonçalves', idade=27)

print("---------- FINAL DE *KWARGS ---------")
print("---------------------------------------------------------------------------------------------------------------")
