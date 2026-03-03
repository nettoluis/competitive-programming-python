2234
'''Coletar a quantidade de cachorros quentes consumidos no total e a quantidade de participantes e retornar a média com até duas casas decimais de precisão'''
quantidadeCachorrosQuentes, quantidadeParticipantes = map(int,input().split())
print(f'{quantidadeCachorrosQuentes / quantidadeParticipantes:.2f}')