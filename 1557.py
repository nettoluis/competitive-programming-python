1557
"""Coletar a ordem de uma matriz quadrada em que cada número abaixo é o dobro do superior"""
while True:
    ordem = int(input())
    if ordem == 0:
        break
    else:
        matriz = [[0] * ordem for _ in range(ordem)]
        for i in range(ordem):
            for j in range(ordem):
                matriz[0][0] = 1
                if j == 0 and i > 0:
                    matriz[i][j] = 2 * matriz[i - 1][0]
                elif i + j > 0 and j != 0:
                    matriz[i][j] = 2 * matriz[i][j - 1]
        for i in matriz:
            print(" ".join(map(lambda x: f'%{len(str(matriz[-1][-1]))}d' % x, i)))
        print("")