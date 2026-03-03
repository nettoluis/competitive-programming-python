linhas, colunas = [int(x) for x in input().split()]

matriz, inverter = [], False
for i in range(linhas):
    if i % 2 == 0:
        matriz.append('#' * colunas)
    else:
        if not inverter:
            matriz.append(('.' * (colunas - 1) + '#'))
            inverter = True
        else:
            matriz.append('#' + '.' * (colunas - 1))
            inverter = False
for linha in range(linhas):
    print(f'{"".join(matriz[linha])}')

