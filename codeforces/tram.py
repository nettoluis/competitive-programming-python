quantidadeParadas, capacidadeMaxima, capacidade = int(input()), 0, 0
for parada in range(quantidadeParadas):
    saidas, entradas = [int(x) for x in input().split()]
    capacidade -= saidas
    capacidade += entradas
    if capacidade > capacidadeMaxima:
        capacidadeMaxima = capacidade
print(capacidadeMaxima)
