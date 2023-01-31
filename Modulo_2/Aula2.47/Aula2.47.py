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
from random import randint
from typing import Any

while True:

    cpf = str(randint(100000000, 999999999))

    cpf_temp = []

    for r in cpf:
        cpf_temp.append(int(r))

    soma_temp = 0

    for r in range(len(cpf_temp)):
        soma_temp = soma_temp + (cpf_temp[r] * ((len(cpf_temp) + 1) - r))

    soma_temp = 11 - (soma_temp % 11)

    if soma_temp > 9:
        cpf_temp.append(0)
    else:
        cpf_temp.append(soma_temp)

    soma_temp = 0

    for r in range(len(cpf_temp)):
        soma_temp = soma_temp + (cpf_temp[r] * ((len(cpf_temp) + 1) - r))

    soma_temp = 11 - (soma_temp % 11)

    if soma_temp > 9:
        continue
    else:
        cpf_temp.append(soma_temp)
        cpf = ''
        for i, valor in enumerate(cpf_temp):
            if i == 3 or i == 6:
                cpf += '.'
            if i == 9:
                cpf += '-'

            cpf += str(valor)
        print(cpf)
        break


