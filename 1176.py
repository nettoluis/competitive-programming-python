1176
"""Coletar o número de casos que serão analisados. Posteriormente, indicar o número da sequência de Fibonacci"""
qtd = int(input())
for _ in range(qtd):
    indiceTermo = int(input())
    fibonacci = [0, 1]
    for i in range(indiceTermo):
        fibonacci.append(fibonacci[-1]+ fibonacci[-2])
    print(f'Fib({indiceTermo}) = {fibonacci[indiceTermo]}')