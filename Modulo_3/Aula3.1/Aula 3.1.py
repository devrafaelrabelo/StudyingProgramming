#
# Funções - DEF em Python (PARTE - 1)
#

def funcao():
    print("Hello World!")

funcao()
funcao()
funcao()
funcao()


def funcao(msg):
    print(msg)

msg = "Meu ovo"
funcao(msg)

funcao(10)
funcao('Meu ovo  2')
funcao(0.5456)

def saudacao(nome='User', msg='Olá'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(f'{nome}, {msg}')


msg_1 = 'Bom dia!!'
nome_1 = 'Rafael Rabelo'

saudacao(nome_1, msg_1)
saudacao(nome='Rayane')
saudacao(nome='Rayane', msg='Hakuna Matata')
saudacao(msg='Hi!!')
saudacao('Roger', 'Boa noite!!')


def saudacao(nome='User', msg='Olá'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{nome} | {msg}'


msg_1 = 'Bom dia!!'
nome_1 = 'Rafael Rabelo'

variavel = saudacao('Roger Rabelo', 'Buenos Dias')

print(variavel)