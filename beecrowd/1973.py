1973
'''Coletar a quantidade de fazendas e a quantidade de carneiros em cada uma das fazendas. Posteriormente, imprimir quantas fazendas foram visitadas e quantos carneiros não foram roubados'''
import sys
def main():
    input = sys.stdin.read
    data = input().split()
    quantidadeFazendas = int(data[0])
    quantidadeCarneirosFazenda = list(map(int, data[1:quantidadeFazendas + 1]))
    visitacaoFazendas = [False] * quantidadeFazendas
    i = 0
    carneirosRoubados = 0
    while 0 <= i < quantidadeFazendas:
        if not visitacaoFazendas[i]:
            visitacaoFazendas[i] = True
        if quantidadeCarneirosFazenda[i] > 0:
            if quantidadeCarneirosFazenda[i] % 2 == 1:
                quantidadeCarneirosFazenda[i] -= 1
                carneirosRoubados += 1
                i += 1
            else:
                quantidadeCarneirosFazenda[i] -= 1
                carneirosRoubados += 1
                i -= 1
        else:
            break
    fazendasVisitadas = sum(visitacaoFazendas)
    quantidadeCarneirosOriginal = sum(quantidadeCarneirosFazenda) + carneirosRoubados
    carneirosNaoRoubados = quantidadeCarneirosOriginal - carneirosRoubados
    print(fazendasVisitadas, carneirosNaoRoubados)
if __name__ == "__main__":
    main()