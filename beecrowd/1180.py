1180
"""Coletar um número inteiro que indicará o tamanho do vetor e imprimir depois o menor valor e a posição dele"""
tamanhoVetor = int(input())
vetores = list(map(int,input().split()))
menorValor = min(vetores)
print(f'Menor valor: {menorValor}\nPosicao: {vetores.index(menorValor)}')