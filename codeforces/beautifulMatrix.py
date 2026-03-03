matriz = []
for linha in range(5):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == 1:
            print(abs(2 - linha) + abs(2 - coluna))
