quantidadeSoldados = int(input())
listaAlturas = [int(x) for x in input().split()]

if quantidadeSoldados == 1:
    print(0)
else:
    maiorAltura, menorAltura = max(listaAlturas), min(listaAlturas)

    posicaoMaior, posicaoMenor = 0, 0
    for i in range(quantidadeSoldados):
        if listaAlturas[i] == maiorAltura:
            posicaoMaior = i
            break 
    for j in range(quantidadeSoldados - 1, -1, -1): 
        if listaAlturas[j] == menorAltura: 
            posicaoMenor = j
            break 

    distanciaComum = posicaoMaior + (quantidadeSoldados - 1) - posicaoMenor

    print(distanciaComum) if posicaoMaior < posicaoMenor else print(distanciaComum - 1)
