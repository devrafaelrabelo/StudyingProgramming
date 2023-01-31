#
# indices
# 0123456789 ....................... 33

frase = 'o Rato roeu a roupa do rei de roma'
tamanha_frase = len(frase)
cont = 0
nova_string = ''
while cont < len(frase):
    if frase[cont] != ' ':
        nova_string += frase[cont]
    else:
        frase[cont] == ' '
        nova_string += '_'

    cont += 1
print(frase)
print(nova_string)
frase = nova_string
print(frase)

