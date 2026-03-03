def calculaTempo(h1, m1, h2, m2):
    instanteInicial, instanteFinal = (h1  * 60) + m1, (h2 * 60) + m2
    if instanteFinal <= instanteInicial:
        return (1440 - instanteInicial) + instanteFinal
    else:
        return instanteFinal - instanteInicial


def main():
    horaInicial, minutoInicial, horaFinal, minutoFinal = [int(x) for x in input().split()]

    tempo = calculaTempo(horaInicial, minutoInicial, horaFinal, minutoFinal)
    horas, minutos = tempo // 60, tempo % 60


    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')


main()
