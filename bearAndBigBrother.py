limakWeight, bobWeight = [int(peso) for peso in input().split()]
anosPassados = 0
while limakWeight <= bobWeight:
    limakWeight *=3
    bobWeight *=2
    anosPassados += 1
print(anosPassados)
