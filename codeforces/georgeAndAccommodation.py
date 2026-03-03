quantidadeQuartos, quartosComVaga = int(input()), 0
for quarto in range(quantidadeQuartos):
    ocupados, capacidade = [int(x) for x in input().split()]
    quartosComVaga += 1 if (capacidade - ocupados) >= 2 else 0
print(quartosComVaga)

