1164
"""Coletar um número inteiro que indicará a quantidade de casos testes. Posteriormente, identificar se um número é perfeito ou não, ou seja, se todos os seus divisores somados dão ele mesmo"""
qtd = int(input())
for _ in range(1, qtd + 1):
    numAnalisado, somaDivisoresProprios = int(input()),0
    for num in range(1, numAnalisado):
        if numAnalisado % num == 0:
            somaDivisoresProprios += num
    print(f'{numAnalisado} eh perfeito') if somaDivisoresProprios == numAnalisado else print(f'{numAnalisado} nao eh perfeito')
