def main():
    n = int(input())

    matriz = []
    for _ in range(n):
        linha = [int(x) for x in input().split()]
        matriz.append(linha)

    somas_prefixo = [[0] * n for _ in range(n)]

    for i in range(n):
        soma_atual = 0
    for j in range(n):
        soma_atual += matriz[i][j]
        somas_prefixo[i][j] = soma_atual

    for i in range(n - 2, -1, -1):
        for j in range(n - i):
            if j == 0:
                peso_base = somas_prefixo[i][j + i]
            else:
                peso_base = somas_prefixo[i][j + i] - somas_prefixo[i][j - 1]
            custo_sub_piramide = min(matriz[i + 1][j], matriz[i + 1][j + 1])
            matriz[i][j] = peso_base + custo_sub_piramide

    print(matriz[0][0])


main()
