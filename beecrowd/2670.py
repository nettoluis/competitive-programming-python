def menor(a, b, c):
    menor = a * b * c
    for elemento in a, b, c:
        if elemento < menor:
            menor = elemento

    return menor


def calculaMenorTempo(sequencia):
    caso1 = (sequencia[1] * 2) + (sequencia[2] * 4)
    caso2 = (sequencia[0] * 2) + (sequencia[2] * 2)
    caso3 = (sequencia[0] * 4) + (sequencia[1] * 2)

    return menor(caso1, caso2, caso3)


def main():
    andares = []
    for _ in range(3):
        pessoas = int(input())
        andares.append(pessoas)
    
    tempoMinimo = calculaMenorTempo(andares)

    print(tempoMinimo)


main()
