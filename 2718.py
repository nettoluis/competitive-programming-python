def contaUns(sequencia):
    contador, maior = 0, 0
    for elemento in sequencia:
        if elemento == '1':
            contador += 1
        else:
            if contador > maior:
                maior = contador
            contador = 0
        if contador > maior:
            maior = contador

    return maior


def main():
    qtd = int(input())

    for _ in range(qtd):
        sequencia = f'{int(input()):b}'

        print(contaUns(sequencia))


main()
