def main():
    qtd = int(input())

    for _ in range(qtd):
        x, n = map(int, input().split())

        if not n % 2:
            print(0)
        else:
            print(x)


main()
