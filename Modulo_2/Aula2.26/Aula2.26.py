# ----------------------------------------------------------------------------------------------------------------------

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

# ----------------------------------------------------------------------------------------------------------------------
# Numero e Positivos (somente numeros)
print("\nisnumeric()")
print(num1.isnumeric())
print(num2.isnumeric())

# ----------------------------------------------------------------------------------------------------------------------
# Numero e Positivos (somente numeros)
print("\nisdigit()")
print(num1.isdigit())
print(num2.isdigit())

# ----------------------------------------------------------------------------------------------------------------------
# Numero e Positivos (somente numeros)
print("\nisdecimal()")
print(num1.isdecimal())
print(num2.isdecimal())
# ----------------------------------------------------------------------------------------------------------------------
# Numero e Positivos (somente numeros)

print("\nCalculadora")
if num1.isdigit() and num2.isdigit():
    print("Fazendo conta...")
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Dados Invalidados")

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo com TRY

print("\nCalculadora")

try:
    print("Fazendo conta...")
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print("Dados Invalidados")