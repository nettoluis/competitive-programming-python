def contaVizinhos(matriz, ilin, icol):
    soma = 0
    soma += matriz.get((ilin - 1, icol), 0)
    soma += matriz.get((ilin + 1, icol), 0)
    soma += matriz.get((ilin, icol - 1), 0)
    soma += matriz.get((ilin, icol + 1), 0)

    return str(soma)


def main():
    while True:
        try:
            nlins, ncols = [int(x) for x in input().split()]
            matriz = {}
            for ilin in range(nlins):
                linha = [int(x) for x in input().split()]
                for i in range(len(linha)):
                    matriz[(ilin, i)] = linha[i]

            mensagem = ''
            for ilin in range(nlins):
                for icol in range(ncols):
                    if matriz[(ilin, icol)] == 1:
                        mensagem += '9'
                    else:
                        mensagem += contaVizinhos(matriz, ilin, icol)
                    if icol == (ncols - 1) and ilin != (nlins - 1):
                        mensagem += '\n'
            print(mensagem)
        except EOFError:
            break


main()
