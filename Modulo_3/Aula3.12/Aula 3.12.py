print()
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {'a': '4', 'b': '101', 'c': '6', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
            'pergunta': 'Quanto é 100x50? ',
            'respostas': {'a': '10000', 'b': '5000', 'c': '5050', },
            'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 4x2? ',
        'respostas': {'a': '8', 'b': '12', 'c': '6', },
        'resposta_certa': 'a',
    },
}

# print("--------------------- COMPLETO PERGUNTAS")
# print(perguntas)
# print("--------------------- ITENS")
# print(perguntas.items())
# print("--------------------- VALUES")
# print(perguntas.values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1")
# print(perguntas['Pergunta 1'])
# print("--------------------- ITENS")
# print(perguntas['Pergunta 1'].items())
# print("--------------------- VALUES")
# print(perguntas['Pergunta 1'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - PERGUNTA")
# print(perguntas['Pergunta 1']['pergunta'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 1']['pergunta'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 1']['pergunta'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - RESPOSTAS")
# print(perguntas['Pergunta 1']['respostas'])
# print("--------------------- ITENS")
# print(perguntas['Pergunta 1']['respostas'].items())
# print("--------------------- VALUES")
# print(perguntas['Pergunta 1']['respostas'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - RESPOSTAS - A")
# print(perguntas['Pergunta 1']['respostas']['a'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 1']['respostas']['a'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 1']['respostas']['a'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - RESPOSTAS - B")
# print(perguntas['Pergunta 1']['respostas']['b'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 1']['respostas']['b'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 1']['respostas']['b'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - RESPOSTAS - C")
# print(perguntas['Pergunta 1']['respostas']['c'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 1']['respostas']['c'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 1']['respostas']['c'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 1 - RESPOSTAS CERTAS")
# print(perguntas['Pergunta 1']['resposta_certa'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 1']['resposta_certa'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 1']['resposta_certa'].values())
#
# # ----------------------------------------------------------------------------------------------------------------------
# print("---------------------------------------------------------------------------------------------------------------")
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2")
# print(perguntas['Pergunta 2'])
# print("--------------------- ITENS")
# print(perguntas['Pergunta 2'].items())
# print("--------------------- VALUES")
# print(perguntas['Pergunta 2'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - PERGUNTA")
# print(perguntas['Pergunta 2']['pergunta'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 2']['pergunta'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 2']['pergunta'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - RESPOSTAS")
# print(perguntas['Pergunta 2']['respostas'])
# print("--------------------- ITENS")
# print(perguntas['Pergunta 2']['respostas'].items())
# print("--------------------- VALUES")
# print(perguntas['Pergunta 2']['respostas'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - RESPOSTAS - A")
# print(perguntas['Pergunta 2']['respostas']['a'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 2']['respostas']['a'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 2']['respostas']['a'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - RESPOSTAS - B")
# print(perguntas['Pergunta 2']['respostas']['b'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 2']['respostas']['b'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 2']['respostas']['b'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - RESPOSTAS - C")
# print(perguntas['Pergunta 2']['respostas']['c'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 2']['respostas']['c'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 2']['respostas']['c'].values())
#
# print('')
# print("--------------------- COMPLETO PERGUNTAS - PERGUNTAS 2 - RESPOSTAS CERTAS")
# print(perguntas['Pergunta 2']['resposta_certa'])
# # print("--------------------- ITENS")
# # print(perguntas['Pergunta 2']['resposta_certa'].items())
# # print("--------------------- VALUES")
# # print(perguntas['Pergunta 2']['resposta_certa'].values())

respostas_certas = 0
for p_keys, p_values in perguntas.items():
    print(f"{p_keys}: {p_values['pergunta']}")

    print('Respostas:')
    for r_keys, r_values in p_values['respostas'].items():
        print(f"[{r_keys}]: {r_values}")

    u_resposta = input("Digite a opção correta: ")

    if u_resposta in p_values['resposta_certa']:
        print("Resposta correta!!")
        respostas_certas += 1
    else:
        print("Resposta Incorreta!!")
    print('')

print(f'Voce acertou {respostas_certas}/{len(perguntas)} das respostas!!!')

respostas_certas = respostas_certas / len(perguntas) * 100
print(f'Voce acertou {respostas_certas}% das respostas!!!')
