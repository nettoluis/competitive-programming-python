def escolheRena(numero):
    nomes = {
        0: 'Rudolph',
        8: 'Blitzen',
        7: 'Donner',
        6: 'Cupid',
        5: 'Comet',
        4: 'Vixen',
        3: 'Prancer',
        2: 'Dancer',
        1: 'Dasher',
}
    
    return nomes[numero]


def soma(s):
    soma = 0
    for e in s:
        soma += e

    return soma


def main():
    bolas = soma([int(x) for x in input().split()])

    print(escolheRena(bolas % 9))


main()
