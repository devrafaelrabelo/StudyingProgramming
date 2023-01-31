#
# Operador OR
#
#
nome = input("Qual seu nome: ")

if nome:
    print(nome)
else:
    print("Você não digitou nada!")

while True:
    nome = input("Qual seu nome: ")
    print(nome or f'Você não digitou nda')

while True:
    nome = input("Qual seu nome: ")
    print(nome or None or False or 0 or f'Você não digitou nda')
