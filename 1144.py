1144
"""Coletar um número inteiro que indicará a metade das linhas impressas no problema. Posteriormente, imprimir o matriz do número elevado a 1, ao quadraddo e ao cubo."""
linhas = int(input())
for num in range(1, linhas + 1, 1):
    print(f'{num ** 1} {num ** 2} {num ** 3}')
    print(f'{num ** 1} {(num ** 2) + 1} {(num ** 3) + 1}')