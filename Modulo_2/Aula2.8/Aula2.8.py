# Dados primitivos - Tipos de Dados

"""
Tipos de dados
str - string = Textos "assim" 'assim'
int - inteiro = Numero inteiros - 10, 50, 5000
float - real/ponto flutuante = Numeros com . - 10.1, 50.5, - 5000.1
bool - booleano/lógico = Verdade ou falso, true ou false 10 == 10 - True, 10 == 5 - False

"""

print('Rafael', type('Rafael'), sep=' = ')
print(150, type(150), sep=' = ')
print(150.5, type(150.5), sep=' = ')
print(10 == 100, type(10 == 100), sep=' = ')
print(10 == 10, type(10 == 10), sep=' = ')
print('l' == 'l', type("l" == "l"), sep=' = ')
print('l' == 'a', type("l" == "a"), sep=' = ')
print(bool(''))
print()
print("Rafael", type("Rafael"), bool('Rafael'), sep=' = ')
print("10", type("10"), type(int('10')), sep=' = ')


# Exercicio

# Nome: String
print("Rafael Rabelo Gonçalves", type("Rafael Rabelo Gonçalves"), sep=':  ')

# Idade: Int
print(27, type(27), sep=':  ')

# Altura: float
print(1.81, type(1.81), sep=':  ')

# É maior de idade 10 > 20
print(18 >= 18, type(18 >= 18), sep=':  ')
