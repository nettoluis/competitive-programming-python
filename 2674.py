def verificaSuper(numero):
    for caractere in str(numero):
        if int(caractere) not in [2, 3, 5, 7]:
            return False

    return True


def geraPrimosESuper(n):
    eh_primo = [True] * (n + 1)

    eh_primo[0], eh_primo[1] = False, False
    for p in range(2, int(n ** 0.5) + 1):
        if eh_primo[p]:
            for i in range(p * p, n + 1, p):
                eh_primo[i] = False

    primos = []
    super_primos = []
    for num in range(2, n + 1):
        if eh_primo[num]:
            primos.append(num)
            if verificaSuper(num):
                super_primos.append(num)

    return set(primos), set(super_primos)


def main():
    primos, superPrimos = geraPrimosESuper(10 ** 5)
    while True:
        try:
            num_teste = int(input())
            if num_teste in superPrimos:
                print('Super')
            elif num_teste in primos:
                print('Primo')
            else:
                print('Nada')
        except EOFError:
            break


main()
