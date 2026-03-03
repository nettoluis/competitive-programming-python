def calculaTempo(n, e1, e2, t1, t2, tr12, tr21, s1, s2):
    c1 = [0] * n
    c2 = [0] * n

    c1[0] = e1 + t1[0]
    c2[0] = e2 + t2[0]

    for i in range(1, n):
        c1[i] = min(c1[i - 1] + t1[i], c2[i - 1] + tr21[i - 1] + t1[i])
        c2[i] = min(c2[i - 1] + t2[i], c1[i - 1] + tr12[i - 1] + t2[i])

    custoFinal = min(c1[n - 1] + s1, c2[n - 1] + s2)

    return custoFinal
        

def main():
    while True:
        try:
            etapas = int(input())
            entrada1, entrada2 = map(int, input().split(maxsplit=2))
            tempos1,= list(map(int, input().split(maxsplit=etapas))), 
            tempos2 = list(map(int, input().split(maxsplit=etapas)))
            transicao12 =  list(map(int, input().split(maxsplit=(etapas - 1))))
            transicao21 = list(map(int, input().split(maxsplit=(etapas - 1))))
            saida1, saida2 = map(int, input().split(maxsplit=2))

            tempoDecorrido = calculaTempo(etapas, entrada1, entrada2, tempos1, tempos2, transicao12, transicao21, saida1, saida2)

            print(tempoDecorrido)
        except EOFError:
            break


main()
