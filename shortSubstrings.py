def reduz(b):
    a = b[0:2]
    for i in range(2, len(b) - 1, 2):
        atual, posterior = b[i], b[i + 1]
        a += posterior

    return a


def main():
    qtd = int(input())

    for _ in range(qtd):
        b = input()
        a = reduz(b)
        print(a)


main()
