1146
"""Coletar um número inteiro e imprimir a sequência de 1 até ele(inclusivo) até receber o número 0"""
while True:
    numEscolhido = int(input())
    if numEscolhido == 0:
        break
    else:
        print(f"{' '.join(str(1 + i) for i in range(0,numEscolhido))}")
