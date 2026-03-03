1134
"""Coletar números referentes ao tipo de combustível(1 - alcool, 2 - gasolina, 3 - diesel) até que o usuário digite o número 4"""
alcool, gasolina, diesel = 0, 0, 0
while True:
    escolhaCombustivel = int(input())
    match escolhaCombustivel:
        case 4:
            break
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
        case _:
            pass
print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')