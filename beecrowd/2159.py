2159
'''Coletar um número inteiro e indicar a quantidade mínima e máxima de primos segundo a fórmula da aproximação da quantidade de primos'''
import math
numeroAnalisado = int(input())
limiteMinimo, limiteMaximo = (numeroAnalisado / (math.log(numeroAnalisado))), 1.25506 * (numeroAnalisado / (math.log(numeroAnalisado)))
print(f'{limiteMinimo:.1f} {limiteMaximo:.1f}')
