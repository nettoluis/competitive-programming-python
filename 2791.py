def encontrarFeijao(sequencia):
    for i in range(len(sequencia)):
        if sequencia[i] == 1:

    return i


def main():
    posicoes = [int(x) for x in input().split()]

    posicao = encontrarFeijao(posicoes) + 1

    print(posicao)


main()
