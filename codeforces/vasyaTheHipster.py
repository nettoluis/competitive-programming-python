vermelhas, azuis = [int(x) for x in input().split()]
estilosos, normais = 0, 0
if vermelhas >= azuis:
    estilosos += azuis
    normais += (vermelhas - azuis) // 2
else:
    estilosos += vermelhas
    normais += (azuis - vermelhas) // 2

print(estilosos, normais)
