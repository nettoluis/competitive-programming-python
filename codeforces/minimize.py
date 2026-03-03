def inteirizador(sequencia):
    for elemento in sequencia:
        elemento = int(elemento)

    return sequencia


def main():
    qtdTestes = int(input())

    for _ in range(qtdTestes):
        a, b = [int(x) for x in input().split()]
        print(b - a)
        

main()
