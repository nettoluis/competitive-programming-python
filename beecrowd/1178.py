1178
"""Coletar um valor flutuante e imprimir a metade dele nas posições subsequentes"""
num = float(input())
for i in range(100):
    print(f'N[{i}] = {num:.4f}')
    num /= 2