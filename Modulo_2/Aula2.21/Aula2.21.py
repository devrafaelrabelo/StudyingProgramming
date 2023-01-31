#
# Operadores Relacionais
# == > >= < <= !=
#

# Exemplo 1 == IGUAL — Pode comparar com STR
print("\nIGUAL")
print(2 == "2")
print(2 == 3)
print(2 == 2)
print('Rafael' == 'Rafael')
print('Rafael' == 'rafael')
print('Rafael' == 'Rabelo')

# Exemplo 2 > MAIOR — Da erro ao se comporar com STR
print("\nMAIOR")
print(2 > 1)
print(2 > 2)
print(2 > 3)
print('Rafael' > 'Rafael')
print('Rafael' > 'rafael')
print('Rafael' > 'Rabelo')

# Exemplo 3 >= MAIOR OU IGUAL — Da erro ao se comporar com STR
print("\nMAIOR OU IGUAL")
print(2 >= 1)
print(2 >= 2)
print(2 >= 3)
print('Rafael' >= 'Rafael')
print('Rafael' >= 'rafael')
print('Rafael' >= 'Rabelo')

# Exemplo 4 < MENOR — Da erro ao se comporar com STR
print("\nMENOR")
print(2 < 1)
print(2 < 2)
print(2 < 3)
print('Rafael' < 'Rafael')
print('Rafael' < 'rafael')
print('Rafael' < 'Rabelo')

# Exemplo 5 <= MENOR OU IGUAL — Da erro ao se comporar com STR
print("\nMENOR OU IGUAL")
print(2 <= 1)
print(2 <= 2)
print(2 <= 3)
print('Rafael' <= 'Rafael')
print('Rafael' <= 'rafael')
print('Rafael' <= 'Rabelo')

# Exemplo 6 - != DIFERENTE — Pode comparar com STR
print("\nIGUAL")
print(2 != "3")
print(2 != "2")
print(2 != 3)
print(2 != 2)
print('Rafael' != 'Rafael')
print('Rafael' != 'rafael')
print('Rafael' != 'Rabelo')

# ----------------------------------------------------------------------------------------------------------------------
num1 = 2
num2 = 1
num4 = 3
num3 = '3'
nome1 = 'Rafael'
nome2 = 'rafael'
nome3 = 'Rabelo'

# Exemplo 1 == IGUAL — Pode comparar com STR
print("\nCom Variaveis")
print("IGUAL")
print(num1 == num3)
print(num1 == num2)
print(num1 == num1)
print(nome1 == nome1)
print(nome1 == nome2)
print(nome1 == nome3)

# Exemplo 2 > MAIOR — Da erro ao se comporar com STR
print("\nMAIOR")
print(num1 > num1)
print(num1 > num2)
print(num1 > num4)
print(nome1 > nome1)
print(nome1 > nome2)
print(nome1 > nome3)

# Exemplo 3 >= MAIOR OU IGUAL — Da erro ao se comporar com STR
print("\nMAIOR OU IGUAL")
print(num1 >= num1)
print(num1 >= num2)
print(num1 >= num4)
print(nome1 >= nome1)
print(nome1 >= nome2)
print(nome1 >= nome3)

# Exemplo 4 < MENOR — Da erro ao se comporar com STR
print("\nMENOR")
print(num1 < num1)
print(num1 < num2)
print(num1 < num4)
print(nome1 < nome1)
print(nome1 < nome2)
print(nome1 < nome3)

# Exemplo 5 <= MENOR OU IGUAL — Da erro ao se comporar com STR
print("\nMENOR OU IGUAL")
print(num1 <= num1)
print(num1 <= num2)
print(num1 <= num4)
print(nome1 <= nome1)
print(nome1 <= nome2)
print(nome1 <= nome3)

# Exemplo 6 - != DIFERENTE — Pode comparar com STR
print("\nIGUAL")
print(num1 != num3)
print(num1 != num1)
print(num1 != num4)
print(num1 != num2)
print(nome1 != nome1)
print(nome1 != nome2)
print(nome1 != nome3)

# Exemplo Aula1.1

nome = input('\nQual o seu nome? ')
idade = int(input("Qual a sua idade? "))

idade_limite_minima = 18


if idade >= idade_limite_minima:
    print(f'Emprestimo concedido para {nome}')
else:
    print(f'Emprestimo nao concedido para {nome}\n')


# Exemplo Aula1.1 Melhorado por mim
print(f'Emprestimo com Maximo e Minimo de idade')

nome = input('Qual o seu nome? ')
idade = int(input("Qual a sua idade? "))

idade_limite_minima = 18
idade_limite_maxima = 30

if idade <= idade_limite_maxima & idade >= idade_limite_minima:
    print(f'Emprestimo concedido para {nome}')
else:
    print(f'Emprestimo nao concedido para {nome}')
