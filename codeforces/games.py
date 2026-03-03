quantidadeTimes = int(input())

casa = []
fora = []

for time in range(quantidadeTimes):
    uniformeUm, uniformeDois = [int(x) for x in input().split()]
    casa.append(uniformeUm)
    fora.append(uniformeDois)

casos = 0
for i in range(quantidadeTimes):
    for j in range(quantidadeTimes):
        if fora[i] == casa[j]:
            casos += 1

print(casos)
