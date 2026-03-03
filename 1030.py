def posicaoSobrevivente(n, k):
    posicao = 1
    for i in range(2, n + 1):
        posicao = (posicao + k - 1) % i + 1

    return posicao


def main():
    qtd = int(input())

    for _ in range(1, qtd + 1):
        n, k = [int(x) for x in input().split()]
        sobrevivente = posicaoSobrevivente(n, k)

        print(f'Case {_}: {sobrevivente}')


main()
