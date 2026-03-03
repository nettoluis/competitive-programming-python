1589
"""Coletar a quantidade de casos que serão analisados e imprimir o menor raio possível de um fio que conterá dois outros fios menores"""
qtd = int(input())
for _ in range(qtd):
    r1, r2 = map(int,input().split())
    print(f'{r1 + r2}')