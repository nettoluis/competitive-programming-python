1866
'''Coletar a quantidade de casos teste e imprimir a soma de uma sequência de quantidadeFazendas números'''
qtdCasos = int(input())
for _ in range(qtdCasos):
    N = int(input())
    print(1) if N % 2 != 0 else print(0)