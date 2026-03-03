def menor(sequencia):
    menor = acumulador(sequencia)
    for elemento in sequencia:
        if elemento <= menor:
            menor = elemento
    return menor


def acumulador(sequencia):
    total = 0
    for elemento in sequencia:
        total += elemento
    return total


def main():
    qtdTestes = int(input())

    for _ in range(qtdTestes):
        numeros = [int(numero) for numero in input().split()]
        total, minimo = acumulador(numeros), menor(numeros)
        condicao = True if total - minimo >= 10 else False
        if condicao: print('YES')
        else: print('NO')


main()
