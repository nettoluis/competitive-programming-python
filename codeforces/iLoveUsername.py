quantidadeNotas = int(input())
notas = [int(x) for x in input().split()]
menor, maior, excelentes = notas[0] , notas[0], 0

for i in range(1, quantidadeNotas):
    if notas[i] < menor:
        menor = notas[i]
        excelentes += 1
    elif notas[i] > maior:
        maior = notas[i]
        excelentes += 1

print(excelentes)
