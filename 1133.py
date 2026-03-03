1133
"""Coletar dois números inteiros que indiquem os limites do espaço amostral, e imprimir todos os números entre eles que possuam resto 2 ou 3 para uma divisão por 5"""
a,b = int(input()), int(input())
if (a < b):
    rangeUtilizado = range(a + 1, b, 1)
else:
    rangeUtilizado = range(b + 1,a,1)
for num in rangeUtilizado:
    print(num) if num % 5 == 2 or num % 5 == 3 else None