from pycodestyle import continued_indentation

1132
"""Coletar dois números e somar todos os números que não são múltiplos de 13 entre eles, não necessariamente em ordem cresce"""
limiteUm, limiteDois, soma, rangeUtilizado = int(input()), int(input()), 0, 0
if limiteUm > limiteDois:
    rangeUtilizado = range(limiteDois, limiteUm + 1)
else:
    rangeUtilizado = range(limiteUm, limiteDois + 1)
for num in rangeUtilizado:
    if num % 13 != 0:
        soma += num
print(soma)

