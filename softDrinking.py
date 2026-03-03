amigos, garrafas, capacidadeGarrafa, limoes, qtdPorLimoes, totalSal, necessidadeBebida, necessidadeSal = [int(x) for x in input().split()]

totalBebidas, totalLimoes = garrafas * capacidadeGarrafa, limoes * qtdPorLimoes
bebidas, limoes, sal = totalBebidas // necessidadeBebida, totalLimoes, totalSal // necessidadeSal

print(min(bebidas, limoes,sal) // amigos)
