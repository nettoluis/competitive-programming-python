def main():
    while True:
        digitos = [0] * 10
        lower, upper = [int(x) for x in input().split()]
        if lower == 0 and upper == 0: break
        for num in range(lower, upper + 1):
            for caractere in str(num):
                digitos[int(caractere)] += 1

        print(f'{" ".join(str(digitos[i]) for i in range(10))}')


main()
