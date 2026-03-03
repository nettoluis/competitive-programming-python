1115
'''Coletar dois números que corresponderão às coordenadas X e Y, respectivamente, e depois imprimir em qual quadrante está localizado'''
while True:
    x, y = map(int,input().split())
    if x != 0 and y != 0:
        if x > 0:
            print('primeiro') if y > 0 else print('quarto')
        else:
            print('segundo') if y > 0 else print('terceiro')
    else:
        break