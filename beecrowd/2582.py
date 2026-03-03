2582
'''Coletar a quantidade de músicas que serão selecionadas. Posteriomente, coletar a soma de dois números e retornar a música'''
setList = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
quantidadeMusicas = int(input())
for _ in range(quantidadeMusicas):
    numeroUm, numeroDois = [int(x) for x in input().split()]
    print(f'{setList[numeroUm + numeroDois]}')