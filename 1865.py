1865
'''Coletar a quantidade de casos testes e informar se a pessoa conseguiu ou não levantar o Mjolnir'''
qtdCasos = int(input())
for _ in range(qtdCasos):
    pessoa, forca = map(str,input().split())
    print('Y') if pessoa == 'Thor' else print('quantidadeFazendas')