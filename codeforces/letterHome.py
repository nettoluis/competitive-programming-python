quantidadeCasos = int(input())
for caso in range(quantidadeCasos):
    quantidadeAVisitar, pontoPartida = [int(x) for x in input().split()]
    posicoes = list(map(int,input().split()))
    if pontoPartida >= posicoes[-1]:
        print(pontoPartida - posicoes[0])
    elif pontoPartida <= posicoes[0]:
        print(posicoes[-1] - pontoPartida)
    else:
        if abs(posicoes[0] - pontoPartida) < abs(posicoes[-1] - pontoPartida):
            print(f'{abs(posicoes[0] - pontoPartida) + abs(posicoes[-1] - posicoes[0])}')
        else:
            print(f'{abs(posicoes[-1] - pontoPartida) + abs(posicoes[-1] - posicoes[0])}')
