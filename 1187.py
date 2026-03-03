1187
"""Coletar um caractere que indicará a operação realizada(soma ou média) da área superior da matriz delimitada pela diagonal principal e secundária"""
operacao, matriz, soma = input(), [], 0
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)
print(matriz)
for i in range(12):
    for j in range(12):
        if j > i and (i + j) < 11:
            soma += matriz[i][j]
            print(matriz[i][j])
print(f'{soma:.1f}') if operacao == 'S' else print(f'{soma/30:.1f}')