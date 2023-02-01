"""
    Exercicio Aula 3.3
"""
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

print('Exercicio 1')
def saudacao(saudacao, nome):

    return f'{saudacao} {nome}'


print(saudacao('Bom dia!!!', 'Rafael Rabelo'))

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""

print('Exercicio 2')
def soma3(n1, n2, n3):
    return n1 + n2 + n3


print(soma3(5, 8, 10))

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

print('Exercicio 3')
def porcen(n1, porc):
    return n1 + (n1 * porc / 100)

print(porcen(500, 90))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

print('Exercicio 4')
def FizzBuzz(n1):
    if not n1 % 3 and not n1 % 5:
        return 'FizzBuzz'
    elif not n1 % 3:
        return 'Buzz'
    elif not n1 % 5:
        return 'Fizz'
    else:
        return 'Numero Invalido'

print(FizzBuzz(15))