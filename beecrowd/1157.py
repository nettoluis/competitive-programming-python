1157
"""Coletar um número inteiro e retornar todos os divisores dele"""
dividendo, divisor = int(input()), 1
for divisor in range(1,dividendo + 1, 1):
    print(divisor) if dividendo % divisor == 0 else None