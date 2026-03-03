1177
"""Coletar um número que será o número limite -- não inclusivo -- que se repetirá por 1000 vezes iniciando no 0"""
num = int(input())
for i in range(1000):
    valor = i % num
    print(f"N[{i}] = {valor}")