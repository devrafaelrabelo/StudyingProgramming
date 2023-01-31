#
# Variveis local e global
#

variavel = 'Valor'

def func():
    print(variavel)

def func_1():
    variavel_2 = 'MEUOVO'
    print(variavel)
    print(variavel_2)


def func_2():
    print(variavel_2)  # Não funciona pq esta em outra função, é uma variavel local


def func_3():
    print(variavel_3)


variavel_3 = 'CSZIN'

func()
func_1()
#func_2()
func_3()