1182
"""Coletar a coluna que será somada ou feita a média e imprimir esse matriz"""
coluna, elementosMatriz, operacao,soma, media = int(input()), [], input(), 0, 0
for _ in range(144):
    elementosMatriz.append(float(input()))
for i in range(coluna, 144, 12):
    soma += elementosMatriz[i]
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    media = soma / 12
    print(f'{media:.1f}')