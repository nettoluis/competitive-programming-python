2060
'''Coletar a quantidade de números que serão analisados e imprimir quantos são múltiplo de 2,3,4 e 5'''
multiplos2, multiplos3, multiplos4, multiplos5, quantidadeNumeros, numerosAnalisaveis = 0, 0, 0, 0, int(input()), list(map(int, input().split()))
for numero in numerosAnalisaveis:
    if numero % 2 == 0:
        multiplos2 += 1
    if numero % 3 == 0:
        multiplos3 += 1
    if numero % 4 == 0:
        multiplos4 += 1
    if numero % 5 == 0:
        multiplos5 += 1
print(f'{multiplos2} Multiplo(s) de 2\n{multiplos3} Multiplo(s) de 3\n{multiplos4} Multiplo(s) de 4\n{multiplos5} Multiplo(s) de 5')