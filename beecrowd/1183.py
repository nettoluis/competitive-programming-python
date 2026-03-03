1183
'''Coletar um caractere que indicará se será realizada a soma ou a média dos termos acima da diagonal principal'''
operacao, matriz, soma = input(), [], 0
for _ in range(0, 12):
    linha = []
    for _ in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)
print(matriz)
for i in range(0, 12):
    for j in range(i + 1,len(matriz[i])):
        soma += matriz[i][j]
        print(matriz[i][j])
print(f'{soma:.1f}') if operacao == 'S' else print(f'{soma/66:.1f}')