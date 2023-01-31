#
# Operadores Logicos
# and, or, not
# in e not in

# E = (&, AND)
print('Exemplo E - and ')
if 10 > 10 and 10== 10:
    print('Os dois são verdadeiro')
else:
    print("Pelo menos um é falso")

# ----------------------------------------------------------------------------------------------------------------------
# OU = or
print('\nExemplo OU - or ')
if 10 >= 10 or 9 == 10:
    print('Algum desses é verdadeiro')
else:
    print("Nenhum é Verdadeiro")

# ----------------------------------------------------------------------------------------------------------------------
# Inversor - not

print('\nExemplo Inversor - not ')
if 10 >= 11:
    print("10 é Maior")
else:
    print("10 é Menor")

print('\nExemplo 2 Inversor - not ')
a = 'a'
b = 1
if not a:
    print("A esta sem valor")
elif a:
    print("Tem valor")
if not b:
    print("A esta sem valor")
elif b:
    print("Tem valor")

# ----------------------------------------------------------------------------------------------------------------------
# INCaseSensitive

nome = "Rafael Rabelo Gonçalves"

if "R" in nome:
    print("Existe")

if "Rafael" in nome:
    print("Existe")

# ----------------------------------------------------------------------------------------------------------------------
# NOT IN - CaseSensitive
if "r" not in nome:
    print("Não existe")
else:
    print("Existe")

if "Gonçalves" not in nome:
    print("Não existe")
else:
    print("Existe")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo Aula1.1 - Sistema simples de login

usurio = input("Digite o username: ")
senha = input("Digite o password")

usurio_bd = "Rafael Rabelo"
senha_bd = "1234567"

if usurio_bd == usurio and senha_bd == senha:
    print("Usuario logado")
else:
    print("Username ou Password invalidado")

