2540
'''Coletar a quantidade de votantes e indicar se haverá impeachment ou não'''
while True:
    try:
        quantidadeVotos = int(input())
        votos = [int(x) for x in input().split()]
        print('impeachment') if votos.count(1) >= (2/3 * quantidadeVotos) else print('acusacao arquivada')
    except EOFError:
        break