1143
"""Coletar um número inteiro que representará a quantidade de linhas impressas. Posteriormente, imprimir o matriz do número elevado a 1, ao quadrado e ao cubo"""
linhas = int(input())
for num in range(1, linhas + 1, 1):
    print(f'{num ** 1} {num ** 2} {num ** 3}')