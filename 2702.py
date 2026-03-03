def calculaNaoAtendidos(disponivel, desejo):
    naoAtendidos = 0
    if desejo > disponivel:
        naoAtendidos += desejo - disponivel 

    return naoAtendidos


def main():
    frangoDisp, bifeDisp, massaDisp = [int(x) for x in input().split()]
    frangoDesej, bifeDesej, massaDesej = [int(x) for x in input().split()]
    
    naoAtendidos = calculaNaoAtendidos(frangoDisp, frangoDesej) + calculaNaoAtendidos(bifeDisp, bifeDesej) + calculaNaoAtendidos(massaDisp, massaDesej)

    print(naoAtendidos)


main()
