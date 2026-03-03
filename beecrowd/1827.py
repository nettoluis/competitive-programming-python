1827
'''Coletar a ordem de uma matriz e imprimí-la, acabando em EOF'''
while True:
    try:
        ordem = int(input())
        matriz, mediana, preenchimentoInterior = [[0] * ordem for _ in range(ordem)], ordem ** 2 // 2, ordem // 3
        for i in range(ordem):
            for j in range(ordem):
                matriz[mediana // ordem][mediana % ordem] = 4
                if (ordem - (1 + preenchimentoInterior)) >= i >= preenchimentoInterior and (ordem - (1 + preenchimentoInterior)) >= j >= preenchimentoInterior:
                    matriz[i][j] = 1
                elif matriz[i][j] == 0 and i == j:
                    matriz[i][j] = 2
                elif matriz[i][j] == 0 and (i + j) == (ordem - 1):
                    matriz[i][j] = 3
        for i in range(ordem):
            print(f'{"".join(map(str,matriz[i]))}')
        print('')
    except EOFError:
        break