totalNiveis = int(input())
xLista = [int(x) for x in input().split()]
xSet = set(xLista[1:])
yLista = [int(x) for x in input().split()]
ySet = set(yLista[1:])
niveisPassados = xSet.union(ySet)
print('I become the guy.') if totalNiveis == len(niveisPassados) else print('Oh, my keyboard!')
