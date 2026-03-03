def ehPrimo(num):
    return num in primos(num)


def primos(n):
    eh_primo = [True] * (n + 1)

    eh_primo[0], eh_primo[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if eh_primo[i]:
            for p in range(i * i, n + 1, i):
                if eh_primo[p]:
                    eh_primo[p] = False

    primos = []
    for i in range(len(eh_primo)):
        elemento = eh_primo[i]
        if elemento:
            primos.append(i)

    return primos


def somaPorSaltos(pilha, salto):
    soma = 0
    for i in range(len(pilha) - 1, -1, -salto):
        soma += pilha[i]

    return soma


def main():
    while True:
        try:
            qtd = int(input())

            pilha = []
            for _ in range(qtd):
                moeda = int(input())
                pilha.append(moeda)

            soma = somaPorSaltos(pilha, int(input()))

            print('Bad boy! I’ll hit you.') if not ehPrimo(soma) else print('You’re a coastal aircraft, Robbie, a large silver aircraft.')

        except EOFError:
            break


main()
