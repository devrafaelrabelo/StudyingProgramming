# Condições IF, ELIF, ELSE

#Ex - 1
if True:
    print("Verdadeiro")
    num_1 = 10
    num_2 = 20
    print(f'{num_1} + {num_2} = {num_1 + num_2}')

# ----------------------------------------------------------------------------------------------------------------------
# Ex - 2
v1 = False

if v1 == True:
    print("Verdade")
else:
    print("Falso")

# ----------------------------------------------------------------------------------------------------------------------
# Ex - 3
if False:
    print("Verdade")
else:
    print("Falso")

# ----------------------------------------------------------------------------------------------------------------------
#Ex - 4
v1 = int(input("Digite o numero: 8"))

if v1 < 5:
    print("Menor que 5")
elif v1 > 5:
    print("Maior que 5")
else:
    print("É igual a 5")







