def encontraMaior(sequencia):
    maior = 0
    for elemento in sequencia:
        if len(elemento) >= maior:
            maior = len(elemento)

    return maior


def encontraSugestoes(sequencia, elemento):
    sugestoes = []
    for palavra in sequencia:
        if len(palavra) >= len(elemento):
            substring = True
            for i in range(len(elemento)):
                if palavra[i] != elemento[i]:
                    substring = False
            if substring:
                sugestoes.append(palavra)
            
    return sugestoes


def main():
    qtd1 = int(input())

    anteriores = []
    for _ in range(qtd1):
        pesquisa = input()
        anteriores.append(pesquisa)

    qtd2 = int(input())
    for _ in range(qtd2):
        novaPesquisa = input()
        sugestoes = encontraSugestoes(anteriores, novaPesquisa)
        if len(sugestoes) == 0:
            print(-1)
        else:
            qtdSugestoes, maiorPalavra = len(sugestoes), encontraMaior(sugestoes)
            print(qtdSugestoes, maiorPalavra)


main()
