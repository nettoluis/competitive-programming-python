2510
'''Coletar a quantidade de vilões e imprimir Y se ele já foi derrotado pelo Batmain'''
quantidadeViloes = int(input())
for _ in range(quantidadeViloes):
    nomeVilao = input()
    print('Y') if nomeVilao.isalpha() else print('N')