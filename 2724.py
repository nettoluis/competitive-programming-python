def copia(sequencia, ini, fim):
    copia = ''
    for i in range(ini, fim):
        copia += sequencia[i]

    return copia


def contem(composto, perigoso):
    if perigoso not in composto:
        return False
    if composto == perigoso:
        return True

    for i in range(len(composto) - len(perigoso) + 1):
        janela = copia(composto, i, i + len(perigoso))
        if janela == perigoso:
            if i + len(perigoso) == len(composto) or (not composto[i + len(perigoso)].isdigit() and not composto[i + len(perigoso)].islower()):
                return True

    return False
    

def prosseguir(composto, perigosos):
    for perigoso in perigosos:
        if contem(composto, perigoso):
            return False

    return True


def main():
    qtd = int(input())

    for caso in range(qtd):
        qtdPerigosos = int(input())

        perigosos = []
        for _ in range(qtdPerigosos):
            composto = input()
            perigosos.append(composto)

        qtdExperimentos = int(input())
        for _ in range(qtdExperimentos):
            experimento = input()
            print('Prossiga') if prosseguir(experimento, perigosos) else print('Abortar')

        if caso != (qtd - 1): print('')

main()
