#
# Dicionário python
#

import copy

print('\nRegistrando Chave no Dic')
d1 = {'chave_1': 'Valor da chave'}
print(d1, type(d1))

print('\nAdicionando chave ao dic')
d1['chave_2'] = 123456
print(d1, type(d1))

print('\nAtualizando chave_1')
d1['chave_1'] = 654321
print(d1, type(d1))

print('\nAtualizando chave_1')
d1 = dict(chave_1='Valor da chave')
print(d1, type(d1))

print('\nAtualizando chave_2 ao dic')
d1['chave_2'] = 123456
print(d1, type(d1))

print('\nAtualizando chave_1')
d1['chave_1'] = 123456
print(d1, type(d1))

print('\nAtualizando o dic por inteiro')
d1 = {'str': 'String',
      0: 'Inteiro',
      (1, 2, 3, 4): 'Tuplas'}

print('\nVarias maneiras de imprimir DIC')
print(d1, type(d1))
print(d1[0], type(d1))
print(d1['str'], type(d1))
print(d1[(1, 2, 3, 4)], type(d1))

print('\nVarias maneiras de imprimir DIC')
if not 1 in d1:
    print(d1)
    d1[1] = 123456789
    print(d1)
else:
    print("Não Existe")

print('\nAdicionando chave ao dic')
d1.update({'nova_chave': 'novo_valor'})

print('\nBuscando a chave pelo metodo GET')
if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))

print('\nDeletando chave do dic')
del d1[1, 2, 3, 4]

print('\nBuscando se valores realmente existe no dic')
print(d1)
print('str' in d1)
print('str' in d1.keys())
print('n' in d1.values())
print('novo_valor' in d1.values())
print(len(d1), '\n')

print('\nImprimindo chave')
for k in d1:
    print(k)

print('\nImprimindo chave')
for v in d1:
    print(v)

print('\nImprimindo dic por completo')
for k in d1.items():
    print(k)

print('\nImprimindo dic por completo mas itens separados')
for k in d1.items():
    print(k[0], k[1])

print('\nImprimindo dic como Tuplas')
for k, v in d1.items():
    print(k, v)

print('\nCriando Dic, Clientes')

clientes = {
    'Clientes_1': {
        'nome': 'Rafael',
        'sobrenome': 'Rabelo',
    },
    'Clientes_2': {
        'nome': 'Rayane',
        'sobrenome': 'Porto',
    },
    'Clientes_3': {
        'nome': 'Isabelle',
        'sobrenome': 'Penna',
    }
}

print('Imprimindo Dados clientes')
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')  # "\T"Imprimir com espaço de identação

d2 = {1: 'a', 2: 'b', 3: 'c', 4: ['Rayane', 'Porto']}

print('\n Copiando Dic')
v = d2  # Isso não esta criando um copia do arquivo, isso esta trasformando d2 em v, mas os dois sao o mesmo
# objeto se alterar um altera o outro
v[1] = "Roger"
print(d2)
print(v)

print('\nCopiando Dic, com COPY')
v[1] = "Rafael"
v = d2.copy()
v[1] = "Roger"
print(d2)
print(v)

print('\nModificando com UPDATE, Dic Principal')
d2.update({4: ['TabaiPrincipalUPDATE', "Otavio"]})
print(d2)
print(v)

print('\nModificando com UPDATE, Dic Copia')
v.update({4: ['TabaiCopiaUPDATE', "Otavio"]})
print(d2)
print(v)

print('\nModificando pelo indice, Principal')
print('')
d2[4][0] = 'JoaozinhoPrincipalIndice'
print(d2)
print(v)

print('\nModificando pelo indice, Copia')
print('')
v[4][0] = 'JoaozinhoCopiaIndice'
print(d2)
print(v)

print()
print('Copiando com DEEPCOPY')
v1 = copy.deepcopy(d2)
print(d2)
print(v1)

print()
print('\nModificando com UPDATE, Dic Principal DEEPCOPY')
d2.update({4: ['TabaiUpdateCopyDeepcopy', "Otavio"]})
print(d2)
print(v1)

print()
print('\nModificando com INDICE, Dic COPIA DEEPCOPY')
v1[4][0] = 'TabaiPrincipalUPDATE'
print(d2)
print(v1)

print('\nTransformando lista em Dic')

lista = [
    ['c1', (1, 'C1STR')],
    ['c2', (2, 'C2STR')],
    ['c3', 3],
]

print(lista, type(lista))

lista = dict(lista)
print(lista, type(lista))

print('\nTransformando Tuplas em Dic')
n_tuplas = (
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
)

print(n_tuplas, type(n_tuplas))

n_tuplas = dict(n_tuplas)
print(n_tuplas, type(n_tuplas))

print('\nNovo Dict')
dic_new = {
    1: "v1",
    2: "v2",
    3: "v3",
    4: 'v4'
}
print(dic_new)

print('\nNRemovendo com POP, valor da chave 2')
dic_new.pop(2)  # Excluir por KEYs
print(dic_new)


print('\nRemovendo com popitem. remove a ultima chave')
dic_new.popitem()  # Excluir o ultimo
print(dic_new)


print('\nNovo Dict_2')
dic_new_2 = {
    5: "v5",
    6: "v6",
    7: "v7",
    8: 'v8'
}
print(dic_new_2)


print('\nConcatenando os dois dict ')
dic_new.update(dic_new_2)
print(dic_new)
