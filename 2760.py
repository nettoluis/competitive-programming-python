def main():
    a, b, c = input(), input(), input()

    print(a + b + c)
    print(b + c + a)
    print(c + a + b)
    print(f'{a[:10]}{b[:10]}{c[:10]}')


main()
