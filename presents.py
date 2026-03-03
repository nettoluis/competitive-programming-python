quantidadeAmigos = int(input())
destino = [int(x) for x in input().split()]
origem = [0] * quantidadeAmigos
for i in range(quantidadeAmigos):
    origem[i] = destino.index(i + 1) + 1
print(' '.join(str(origem[i]) for i in range(quantidadeAmigos)))
