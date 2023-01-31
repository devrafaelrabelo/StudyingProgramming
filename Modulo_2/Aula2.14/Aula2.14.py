# Formatação de String

nome = "Rafael = "  # Declarar variavel.
idade = 27
altura = 1.81
maior_de_idade = idade >= 18
peso = 63


print("Nome:  ", nome, type(nome))
print("Idade: ", idade, type(idade))
print("Altura: ", altura, type(altura))
print("É maior de Idade: ", maior_de_idade, type(maior_de_idade))
print("Peso: ", peso, type(peso))

imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos e seu imc é', imc)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')

print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))


