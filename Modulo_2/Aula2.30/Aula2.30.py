#
# Formatando valores com modificadores
# :s - Texto (Strings)
# :d - Interios (INT)
# :f - Numeros de ponto Flutuantes (float)
# :. (NUMERO) f - Quantidade de casas decimais (float)
# (CARACTERE) (< > ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
# > - Esquerda
# < - Direita
# ^  Centro
#
# Variaveis
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
# Float
print("Testes com FLOAT :.F")
print(divisao)
print(f'{divisao:.2f}')
print('{:.2f}'.format(divisao))

# String
print("\nTestes com STRING :S")
nome = 'Rafael'
print(nome)
print(f'{nome:s}')

# Acrescenta numero e letras função ( : < > ^ ) - nao pode ser usado numeros > = que 10
num_1 = 10
num_2 = 1150
num_3 = 22
print("\nAcrescentado numeros e letras")
print(f'{num_1:0>10}')
print(f'{num_2:a<10}')
print(f'{num_3:1^10}')

print("\nAcrescentado numeros e letras depois do ponto")
print(f'{num_1:.2f}')
print(f'{num_2:a<10.2f}')
print(f'{num_3:a>10.1f}')
print(f'{num_1:a^10.1f}')
print(f'{nome:#^50}')

print("\nFunção .format")

# nome_formatado = '{:@^50}'.format(nome)
# nome_formatado = '{n:@>24}'.format(n=nome)
# nome_formatado = '{n:@>24} {n:#<24}'.format(n=nome)


# print(f'Normal:  {nome}')
# print(f'Formatado: {nome_formatado}')
nome = 'RAfaEl rAbelO'

print(nome)  # Tudo minusculo
print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculas
print(nome.title())  # Primeiras letras maiusculas


