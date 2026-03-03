1158
"""Coletar um número inteiro que indica a quantidade de casos analisados. Posteriormente, coletar o número de ímpares consecutivos que serão somados e o número de início -- incluí-lo se ele for ímpar"""
qtd = int(input())
for _ in range(1,qtd + 1):
    soma = 0
    num, qtdImpares = map(int,input().split())
    while qtdImpares > 0:
        if num % 2 == 0:
            num += 1
        else:
            soma += num
            num += 2
            qtdImpares -= 1
    print(soma)