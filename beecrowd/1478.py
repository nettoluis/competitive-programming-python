1478
"""Coletar a ordem da matriz até que ela seja igual a 0 e imprimir uma matriz característica"""
while True:
    ordem = int(input())
    if ordem == 0:
        break
    else:
        numPosDiagonalPrincipal = 2
        matriz = [[0] * ordem for _ in range(ordem)]
        for i in range(ordem):
            numPosDiagonalPrincipal, numAntesDiagonalPrincipal = 2, i + 1
            for j in range(ordem):
                if i == j:
                    matriz[i][j] = 1
                elif i < j:
                    matriz[i][j] = numPosDiagonalPrincipal
                    numPosDiagonalPrincipal += 1
                else:
                    matriz[i][j] = numAntesDiagonalPrincipal
                    numAntesDiagonalPrincipal-= 1
        for i in matriz:
            print(" ".join(map(lambda x: "%3d" % x, i)))
        print("")
