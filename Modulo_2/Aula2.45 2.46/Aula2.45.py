"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while True:
    cpf_temp = []
    cpf = input('Digite o CPF: ')
    if not len(cpf) == 14:
        print('CPF - Invalido')
        continue

    for index, valor in enumerate(cpf):
        if not valor.isnumeric():
            if index == 3 and valor == '.':
                # cpf_temp.append(valor)
                continue
            if index == 7 and valor == '.':
                # cpf_temp.append(valor)
                continue
            if index == 11 and valor == '-':
                # cpf_temp.append(valor)
                continue
            else:
                break
        cpf_temp.append(int(valor))

    if not len(cpf_temp) == 11:
        print('CPF - Invalido')
        continue

    soma_temp = 0

    for r in range(len(cpf_temp) - 2):
        soma_temp = soma_temp + (cpf_temp[r] * (10 - r))

    soma_temp = 11 - (soma_temp % 11)

    if soma_temp > 9:
        cpf_temp[9] = 0
    else:
        cpf_temp[9] = soma_temp

    if not cpf[12] != cpf_temp[9]:
        print('CPF - Invalido')
        break

    soma_temp = 0
    for r in range(len(cpf_temp) - 1):
        soma_temp = soma_temp + (cpf_temp[r] * (11 - r))

    soma_temp = 11 - (soma_temp % 11)

    if soma_temp < 9:
        cpf_temp[10] = soma_temp

    if not cpf[13] != cpf_temp[10]:
        print('CPF - Invalido')
        break
    else:
        print('CPF - VALIDO')
