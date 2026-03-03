#Primeira solução
quantidadeAmigos, alturaCerca = [int(x) for x in input().split()]
alturas = [int(altura) for altura in input().split()]
comprimentoCerca = 0
for altura in alturas:
    comprimentoCerca += 2 if altura > alturaCerca else 1
print(comprimentoCerca)
#Segunda solução
quantidadeAmigos, alturaCerca = [int(x) for x in input().split()]
alturas = [int(altura) for altura in input().split()]
comprimentoCerca = sum([1 if altura <= alturaCerca else 2 for altura in alturas])
print(comprimentoCerca)
