1179
"""Coletar valores inteiros e imprimir se eles são pares ou ímpares preenchendo 5 posições e depois imprimindo o restante, primeiro dos ímpares e depois dos pares"""
par, impar = [], []
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            for i in range(5):
                print(f'par[{i}] = {par[i]}')
            par = []
    else:
        impar.append(num)
        if len(impar) == 5:
            for i in range(5):
                print(f'impar[{i}] = {impar[i]}')
            impar = []
for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')
for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')