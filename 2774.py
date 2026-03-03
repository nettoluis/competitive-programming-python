def calculaMedia(sequencia, qtd):
    soma = 0
    for e in sequencia:
        soma += e

    return (soma / qtd)


def calculaPrecisao(sequencia):
    qtd = len(sequencia)
    media = calculaMedia(sequencia, qtd)

    resultado = 0
    for e in sequencia:
        resultado += (e - media) ** 2
    resultado /= (qtd - 1)

    return (resultado ** 0.5)
    

def main():
    while True:
        try:
            horas, minutos = map(int, input().split())
            valores = [float(x) for x in input().split()]
            print(f'{calculaPrecisao(valores):.5f}')
        except EOFError:
            break


main()
