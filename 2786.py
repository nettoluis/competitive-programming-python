def contaT1(areaRestante, AREA_T1):
    return round(areaRestante / AREA_T1)


def contaT2(largura, comprimento):
    return ((largura - 1) * 2) + ((comprimento - 1) * 2)


def main():
    AREA_T1, QTD_T3 = (1 / 1.41421356) ** 2, 4
    AREA_T2, AREA_T3 = AREA_T1 / 2, AREA_T1 / 4
    largura, comprimento = int(input()), int(input())
    areaTotal = largura * comprimento

    unidadesT2 = contaT2(largura, comprimento)
    areaRestante = areaTotal - ((AREA_T2 * unidadesT2) + (AREA_T3 * QTD_T3))
    unidadesT1 = contaT1(areaRestante, AREA_T1)

    print(unidadesT1)
    print(unidadesT2)


main()
