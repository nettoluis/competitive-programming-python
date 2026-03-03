1154
"""Coletar números inteiros até que seja digitado um número negativo e imprimir a média de todos os números inteiros positivos coletados"""
soma, quantidade = 0,0
while True:
    idade = int(input())
    if idade >= 0:
        soma += idade
    else:
        break
    quantidade += 1
media = soma/quantidade
print(f'{media:.2f}')