2334
'''Coletar a quantidade de patinhos que saíram para passear e retornar a quantidade que voltaram.'''
while True:
    quantidadePatinhosForamPassear = int(input())
    if quantidadePatinhosForamPassear == -1:
        break
    else:
        print(quantidadePatinhosForamPassear - 1) if quantidadePatinhosForamPassear >= 1 else print(0)