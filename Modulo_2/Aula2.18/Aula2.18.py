
"""

Aula1.1 Entrada de Dados

"""

# Entrada de Dados STR
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

ano_nascimento = 2022 - int(idade)  # Casting de dados

print(f"{nome} tem {idade} anos e nasceu em {ano_nascimento}")

# Calculadora
# Metodo entrando com STR
num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")
print(f'{num1} + {num2} = {int(num2) + int(num1)}')

# Metodo entrando ja com Número INT
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print(f'{num1} + {num2} = {num2 + num1}')