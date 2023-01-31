#
# While / Else
# Contadores
# Acumuladores
#
contador = 1
acumulador = 1

while contador <= 50 and acumulador < 50:
    print(f'Acumulador: {acumulador}')
    print(contador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Não entrou ')

