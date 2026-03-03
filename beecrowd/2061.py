2061
'''Coletar a quantidade inicial de abas, a quantidade de ações realizadas e quantas abas finais ficarm abertas'''
quantidadeAbas, acoes = map(int,input().split())
for _ in range(acoes):
    acao = input()
    quantidadeAbas += 1 if acao == 'fechou' else -1
print(quantidadeAbas)