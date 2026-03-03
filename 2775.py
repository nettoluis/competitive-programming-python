def swap(s, i1, i2):
    temp = s[i1]
    s[i1] = s[i2]
    s[i2] = temp


def bubbleSortLike(s1, s2, qtd):
    tempo = 0
    passadas = 0
    while True:
        mudancas = 0
        for i in range(qtd - (1 + passadas)):
            if s1[i] > s1[i + 1]:
                swap(s1, i, i + 1)
                tempo += (s2[i] + s2[i + 1])
                mudancas += 1
        passadas += 1
        if not mudancas: break

    return tempo


def main():
    while True:
        try:
            qtd = int(input())

            numeracoes = list(map(int, input().split()))
            tempos = list(map(int, input().split()))

            tempoNecessario = bubbleSortLike(numeracoes, tempos, qtd)

            print(tempoNecessario)
        except EOFError:
            break


main()
