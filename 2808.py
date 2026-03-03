'''Coletar a posição atual de um cavalo no xadrez e informar se é possível chegar na posição destino ou não'''
posicaoAtual, posicaoDesejada = [x for x in input().split()]
dicionarioColunas = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8
}
colunaAtual, linhaAtual = dicionarioColunas[posicaoAtual[0]], int(posicaoAtual[1])
colunaDesejada, linhaDesejada = dicionarioColunas[posicaoDesejada[0]], int(posicaoDesejada[1])
distanciaColunas, distanciaLinhas = (((colunaDesejada - colunaAtual) ** 2) ** 0.5), (((linhaDesejada - linhaAtual) ** 2) ** 0.5)
print('VALIDO') if (distanciaColunas == 2 and distanciaLinhas == 1) or (distanciaColunas == 1 and distanciaLinhas == 2) else print('INVALIDO')

