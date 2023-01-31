secreta = 'PERFUME'
digitadas = []
chance = 5

print(f'Acerte a palavra, contem {len(secreta)} letras')

while True:
    if chance == 0:
        print("Suas Chances Acabaram")
        break

    print(f'Ja digitadas ----> {digitadas}')
    letra = input('Escreva a letra: ').upper()

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in secreta:
        if letra in digitadas:
            print(f'Errou')
            chance -= 1
        else:
            print(f'Acertou')
            digitadas.append(letra)
    else:
        print(f'Errou')
        digitadas.append(letra)
        chance -= 1

    sec_tempo = ''
    for let_sec in secreta:
        if let_sec in digitadas:
            sec_tempo += let_sec
        else:
            sec_tempo += '*'

    if sec_tempo == secreta:
        print(f'PRONTO!!!!!!!!!! - A palavra era = {secreta} {sec_tempo}')
        break

    print(f'Restam {chance} chances!!\n')
