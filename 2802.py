def calcularBinomios(pontos):
    primeiroBinomio = (pontos * (pontos - 1) * (pontos - 2) * (pontos - 3)) / (4 * 3 * 2)
    segundoBinomio = ((pontos) * (pontos - 1)) / 2

    return primeiroBinomio + segundoBinomio


def main():
    pontos = int(input())

    resultado = int(calcularBinomios(pontos) + 1)

    print(resultado)

main()
