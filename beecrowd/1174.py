1174
"""Coletar 100 valores inteiros e imprimir apenas as posições com valores inferiores ou iguais a 10"""
for i in range(0,100,1):
    num = float(input())
    print(f'A[{i}] = {num}') if num <= 10 else None