def main():
    while True:
        try:
            a, b = [f'{int(x):0{32}b}' for x in input().split()]

            c = ''
            for i in range(32):
                if a[i] != b[i]:
                    c += '1'
                else:
                    c += '0'

            print(int(c, 2))
        except EOFError:
            break


main()
