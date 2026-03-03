def montaBaralho(qtdCartas):
    baralho = []
    for _ in range(qtdCartas):
        carta = [int(x) for x in input().split()]
        baralho.append(carta)
    
    return baralho


def main():
    while True:
        try:
            qtdAtributos = int(input())
            qtdM, qtdL = [int(x) for x in input().split()]

            baralhoM, baralhoL = montaBaralho(qtdM), montaBaralho(qtdL)

            escolhidaM, escolhidaL = [int(x) - 1 for x in input().split()]
            atributo = int(input()) - 1

            atributoM, atributoL =  baralhoM[escolhidaM][atributo],  baralhoL[escolhidaL][atributo]
            if atributoM > atributoL:
                print('Marcos')
            elif atributoM < atributoL:
                print('Leonardo')
            else:
                print('Empate')
        except EOFError:
            break

main()
