1181
"""Coletar a linha que será somada ou feita a média e imprimir esse matriz"""
linha, elementosMatriz, operacao,soma, media = int(input()), [], input(), 0, 0
for _ in range(144):
    elementosMatriz.append(float(input()))
for i in range((linha * 12), (linha + 1) * 12):
    soma += elementosMatriz[i]
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    media = soma / 12
    print(f'{media:.1f}')

1181.2
"""Coletar a linha que será somada ou feita a média e imprimir esse matriz"""
linhaSelecionada, operacao, matriz, soma, media = int(input()), input(), [], 0, 0
for _ in range(12):
    linha = []
    for i in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma += sum(matriz[linhaSelecionada])
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')