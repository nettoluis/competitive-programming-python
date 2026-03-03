2551
'''Coletar a quantidade de treinos. Posteriormente, indicar em quais dias ele quebrou seu recorde de velocidade média'''
while True:
    try:
        quantidadeTreinos, recorde = int(input()), 0
        for dia in range(quantidadeTreinos):
            minutos, distancia = [int(x) for x in input().split()]
            if distancia / minutos > recorde:
                print(dia + 1)
                recorde = distancia / minutos
    except EOFError:
        break
