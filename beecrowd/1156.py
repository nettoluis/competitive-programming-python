1156
"""Calcular a soma de S que é a soma de 1/1 + 3/2 + 5/4 e assim por diante até 39/?"""
soma, dividendo, divisor = 0,1,1
while dividendo <= 39:
    soma += dividendo/divisor
    dividendo += 2
    divisor *= 2
print(f'{soma:.2f}')
