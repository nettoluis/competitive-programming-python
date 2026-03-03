def verificaCompatibilidade(l, a, llim, alim):
    return (l <= llim and a <= alim) or (a <= llim and l <= alim)


def main():
    while True:
        try:
            larguraLim, alturaLim, pedidos = [int(x) for x in input().split()]
            for _ in range(pedidos):
                largura, altura = [int(x) for x in input().split()]

                compativel = verificaCompatibilidade(largura, altura, larguraLim, alturaLim)

                print('Sim') if compativel else print('Nao')
        except EOFError:
            break


main()
