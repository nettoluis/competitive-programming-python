def calculaResistenciaCircuito(circuito):
    soma = 0
    for resistor in circuito:
        if resistor.isdigit():
            soma += int(resistor)
        else:
            resistor = resistor.split('|')
            fatorUm, fatorDois = int(resistor[0].lstrip('(')), int(resistor[-1].rstrip(')'))
            soma += (fatorUm * fatorDois) / (fatorUm + fatorDois)

    return soma


def main():
    while True:
        try:
            circuito = [x for x in input().split('-')]

            resistenciaEquivalente = calculaResistenciaCircuito(circuito)

            print(f'{resistenciaEquivalente:.3f}')

        except EOFError:
            break

main()
