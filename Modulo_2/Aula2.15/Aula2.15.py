"""
 Exercicio Aula1.1 2.15

* Criar variaveis para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (nbaseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String (cmo as chaves)

"""


# Declaraçoes de variaveis

nome = 'Rafael Rabelo Gonçalves'
altura = 1.81
idade = 27
peso = 63
ano_atual = 2022

print(f'{nome} tem {idade}, nasceu em {ano_atual-idade}, pesa {peso}Kg, mede {altura} e seu IMC é {peso / altura**2:.2f}')


