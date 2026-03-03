quantidadeCartas = int(input())
cartas = [int(x) for x in input().split()]
sereja, dima = 0, 0

while len(cartas) > 0:
    maior = max(cartas[0], cartas[-1])
    sereja += maior  
    cartas.remove(maior)
    if len(cartas) == 0:
        break
    maior = max(cartas[0], cartas[-1])
    dima += maior
    cartas.remove(maior)

print(sereja, dima)
    
