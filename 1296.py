1296
'''Coletar o valor das medianas de um triângulo e retornar a área do triângulo utilizando a fórmula de Héron'''
while True:
    try:
        medianas = sorted([float(x) for x in input().split()])
        medianaUm, medianaDois, medianaTres = medianas[0], medianas[1], medianas[2]
        if medianaTres >= (medianaDois + medianaUm):
            print('-1.000')
        else:
            semiPerimetro = (medianaUm + medianaDois + medianaTres) / 2
            area = ((semiPerimetro * (semiPerimetro - medianaUm) * (semiPerimetro - medianaDois) * (semiPerimetro - medianaTres)) ** 0.5) * 4/3
            print(f'{area:.3f}')
    except EOFError:
        break