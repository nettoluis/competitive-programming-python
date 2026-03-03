posicoes = sorted([int(x) for x in input().split()])

distancia = posicoes[2] - posicoes[1] + posicoes[1] - posicoes[0]

print(distancia)
