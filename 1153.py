1153
"""Coletar um número e imprimir o fatorial dele"""
num, resultado = int(input()), 1
for x in range(num,0, -1):
    resultado *= x
print(f'{resultado}')
