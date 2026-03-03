def gastoNecessario(lista, maior):
    total = 0
    for elemento in lista:
        total += (maior - elemento)
    return total


def encontrarMaior(lista):
    maior = 0
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior


def main():
    quantidadeCidadaos = int(input())

    patrimonios = [int(patrimonio) for patrimonio in input().split()]
    maior = encontrarMaior(patrimonios)
    gasto = gastoNecessario(patrimonios, maior)

    print(gasto)


main()
