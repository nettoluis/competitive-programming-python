def geraPrimosESuper(n):
    eh_primo = [True] * (n + 1)

    eh_primo[0], eh_primo[1] = False, False
    for p in range(2, int(n ** 0.5) + 1):
        if eh_primo[p]:
            for i in range(p * p, n + 1, p):
                eh_primo[i] = False

    primos = []
    for num in range(2, n + 1):
        if eh_primo[num]:
            primos.append(num)

    return set(primos)
