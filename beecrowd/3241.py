3241
'''Coletar dois números e somá-los'''
quantidadeCasos = int(input())
for caso in range(quantidadeCasos):
    entrada = input()
    if entrada == 'P=NP':
        print('skipped')
    else:
        a, b = [int(x) for x in entrada.split('+')]
        print(a + b)