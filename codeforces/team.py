quantidadeTestes, quantidadeTestesPossiveis = int(input()), 0
for teste in range(quantidadeTestes):
    capacidadeTime = [int(x) for x in input().split()]
    quantidadeTestesPossiveis += 1 if capacidadeTime.count(1) >= 2 else 0
print(quantidadeTestesPossiveis)
