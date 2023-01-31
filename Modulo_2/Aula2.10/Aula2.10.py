"""
Assim como aprendemos na matematica, operadores tem uma certa
precedencia que pode ser alterada usando parenteses
(como descrito na aula anterior).
Abaixo, segue uma lista mais precisa de quais operadores tem
maior prioridade na hora de realizar contas mais complexas
(de maior para menor precedencia)

# 1 - ( N + N ) = Os parenteses tem a maior precedencia,
contas dentro deles sao realizados primeiro

# 2 - ** = Depois vem a exponenciação

# 3 - * / // % - Na sequencia multiplicação, divisão,
divisão inteiro e módulo -> resto da divisão

#4  + - = Por fim, sma e subtração

Contas com operadoes de mesma precendencia são
realizadas da esquerda para a direita .

Obs: Existem muita mais operadores do que estes em Python
e todos eles tamtem tem precedencia, voce pode conferir no site abaixo
https://docs.python.org/3/reference/expressions.html#operator-precedence

"""

print((23 - 24) * (3 - 254.4) / 10)
print(2 ** 4)


# Video Aula1.1

print('Subtração - =', 10 - 10)
print('Soma + =', 10 + 10)
print('Divisao Inteira // =', 9.9 // 10)
print('Divisao / =',  9.9 / 10)
print('Multiplicação * =', 10 * 10)
print('Módulo % =', 9.9 % 10)
print('Módulo % =', 10 % 10)
print('Exponenciação ** =', 10 ** 3)
print('Parenteses () =', (10 + 10) * 10)
print('Sem Parenteses () =', 10 + 10 * 10)

print('Escrevendo varias vezes.', 10 * '\nTeste')
