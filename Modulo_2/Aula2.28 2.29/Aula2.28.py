""" """
# Exercicios - 3 Unid
#

# Exercicio - 1
"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um numero 
inteiro, informe que não é um numero inteiro
"""

numero = input("Digite um numero inteiro: ")
if numero.isdigit():
    numero = int(numero)
    if not numero % 2:
        print(f'{numero}" é um numero par')
    else:
        print(f'"{numero}" é um numero Impar')
else:
    print(f'Digite um numero interio, "{numero}" não é um numero inteiro')

# ----------------------------------------------------------------------------------------------------------------------
# Exercicio - 2
"""
Faça um programa que pergunte a hora ao usuarioe, baseando-se no horario
descrito, exiba a saudação apropriada.Ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horario = input("Digite somente a hora: ")

if horario.isdigit():
    horario = int(horario)
    if 0 <= horario <= 11:
        print("Bom dia!")
    elif 12 <= horario <= 17:
        print("Boa tarde!")
    elif 18 <= horario <= 23:
        print("Boa noite!")
    else:
        print("Horario Invalido")
else:
    print("Horario Invalido")

# ----------------------------------------------------------------------------------------------------------------------
# Exercicio - 3
"""
Faça um programa que peça o primeiro nome de usuario. Se o nome tiver 4 ltras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu 1º nome: ")

if len(nome) <= 4:
    print("Seu nome é curto!")
elif len(nome) <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é grande!")
