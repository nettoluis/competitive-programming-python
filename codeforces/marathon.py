quantidadeTestes = int(input())

for _ in range(quantidadeTestes):
    emFrente = 0
    distancias = [int(distancia) for distancia in input().split()]
    timur = distancias.pop(0)
    for participante in distancias:
        if participante > timur:
            emFrente += 1
    print(emFrente)
