1534
"""Coletar a ordem de uma matriz que segue a sequencia 123 muito doida. SQN, é fácil."""
while True:
    try:
        ordemMatriz, matriz = int(input()), []
        for linha in range(ordemMatriz):
            matriz.append([0] * ordemMatriz)
        for i in range(ordemMatriz):
            for j in range(ordemMatriz):
                if (i + j) == (ordemMatriz - 1):
                    matriz[i][j] = 2
                elif i == j:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 3
        for i in matriz:
            print("".join(str(i[j]) for j in range(ordemMatriz)))
    except EOFError:
        break
