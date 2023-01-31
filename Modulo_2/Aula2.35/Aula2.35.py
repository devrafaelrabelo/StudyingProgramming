#
# For in - Python
# Iterando Strings com ( for )
# Função range ( range=0, stop, step=1 )

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo -
texto = 'PYTHON'
c = 0
while c < len(texto):
    print(texto[c])
    c+= 1

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo 2
texto = 'PYTHON'
for letra in texto:
    print(letra)

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo 3
texto = 'PYTHON'
for n, letra in enumerate(texto):
    print(letra, n)

# ----------------------------------------------------------------------------------------------------------------------
# Exemplo 4 - RANGE=0, STOP = 0, STEP=1
print("POSITIVO")
for numero in range(0, 10, 1):
    print(numero)

print("NEGATIVO")
for numero in range(20, 0, -1):
    print(numero)

print("TESTANDO LOWER/UPPER")
texto = 'PYTHON'
nova_string = ''
for letra in texto:
    if letra == 'T':
        nova_string += letra.lower()
    elif letra == 'N':
        nova_string += letra.lower()
    else:
        nova_string += letra

print(nova_string)

print("TESTANDO LOWER/UPPER e CONTINUE")
texto = 'PYTHON'
nova_string = ''
for letra in texto:
    if letra == 'T':
        continue
        # Removendo o 'T'
    elif letra == 'N':
        nova_string += letra.lower()
    else:
        nova_string += letra

print(nova_string)


