1145
"""Coletar dois números inteiros que representarão a quantidade de colunas e quantidade de termos, respectivamente"""
colunas, termos = map(int,input().split())
for num in range(1,termos - 1, colunas):
    print(f"{' '.join(str(num + i) for i in range(0, colunas))}")