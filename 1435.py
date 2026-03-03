1435
"""Coletar a ordem de uma matriz quadrada"""
while True:
    ordem = int(input())
    if ordem == 0:
        break
    matriz = [[0] * ordem for _ in range(ordem)]
    for linhas in range((ordem + 1) // 2):
        valor = linhas + 1
        for i in range(linhas, ordem - linhas):
            matriz[linhas][i] = valor
            matriz[ordem - 1 - linhas][i] = valor
            matriz[i][linhas] = valor
            matriz[i][ordem - 1 - linhas] = valor
    for linha in matriz:
        print(" ".join(map(lambda x: "%3d" % x, linha)))
    print("")