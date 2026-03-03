1172
"""Coletar números inteiros e retorna o valor e a posição deles, caso o valor seja negativo ou nulo, retornar 1"""
for i in range(0,10,1):
    num = int(input())
    print(f'X[{i}] = 1') if num <= 0 else print(f'X[{i}] = {num}')