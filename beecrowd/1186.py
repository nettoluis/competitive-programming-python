1186
'''Coletar um caractere que indicará se será realizada a soma ou a média dos termos abaixo da diagonal secundaria'''
operacao, matriz, soma = input(), [], 0
for _ in range(0, 12):
    linha = []
    for _ in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)
print(matriz)
for i in range(12):
    for j in range(12):
        soma += matriz[i][j] if i + j > 11 else 0
        print(matriz[i][j])
print(f'{soma:.1f}') if operacao == 'S' else print(f'{soma/66:.1f}')