def procura(elemento, sequencia):
    for e in sequencia:
        if elemento == e:
            return True

    return False


def buscaCarimbadas(qtd_carimbadas, carimbadas, compradas):
    contador = 0
    for i in range(qtd_carimbadas):
        if procura(carimbadas[i], compradas):
            contador += 1

    return contador


def main():
    total, qtd_carimbadas, qtd_compradas = map(int, input().split())
    carimbadas = [int(x) for x in input().split()]
    compradas = [int(x) for x in input().split()]

    carimbadas_compradas = buscaCarimbadas(qtd_carimbadas, carimbadas, compradas)

    print(qtd_carimbadas - carimbadas_compradas)


main()
