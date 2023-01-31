#
# Manipulando Strings
# String indices
# Fatiamento de Strings
# Funçoes built-in len, abs, type, print, etc...
# Essas funções podem ser usadas diretamente em cada tipo.

# Voce pode conferir tudo isso em.
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/stdtypes.html

# indices positivos [0][1][2][3][4]...
texto = 'Python s2'
print(texto[len(texto)-1])

nova_string = texto[:7]
print(nova_string)
print(len(nova_string))

nova_string = texto[1:7]
print(nova_string)
print(len(nova_string))

nova_string = texto[7:]
print(nova_string)
print(len(nova_string))

# Indices Negativos -...[-5][-4][-3][-2][-1].
print('\nIndices Negativos')

nova_string = texto[-9:]
print(nova_string)
print(len(nova_string))

nova_string = texto[-9:-5]
print(nova_string)
print(len(nova_string))

nova_string = texto[-2:]
print(nova_string)
print(len(nova_string))

# Teste com step de Letras
nova_string = texto[0::4]
print(nova_string)
print(len(nova_string))


