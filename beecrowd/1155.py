1155
"""Calcular o matriz de S, que consiste na soma de 1 + todas as divisões de 1/2,1/3 até 1/100"""
soma, dividendo, divisor = 0, 1, 1
while divisor <= 100:
    soma += dividendo / divisor
    divisor += 1
print(f'{soma:.2f}')