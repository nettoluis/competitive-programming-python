2544
'''Coletar a quantidade de ninjas e indicar qual a quantidade de tecnicas de jutsu do clone das sombras'''
from math import log
while True:
    try:
        quantidadeNinjas = int(input())
        print(f'{log(quantidadeNinjas,2):.0f}')
    except EOFError:
        break
