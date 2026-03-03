1184
'''Coletar um caractere que indicará se será realizada a soma ou a média dos termos abaixo da diagonal principal'''
operacao, matriz, soma = input(), [], 0
for _ in range(0, 12):
    linha = []
    for _ in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)
for i in range(1, 12):
    for j in range(0 ,i):
        soma += matriz[i][j]
print(f'{soma:.1f}') if operacao == 'S' else print(f'{soma/66:.1f}')